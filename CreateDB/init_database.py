#!/usr/bin/env python3

import argparse
import sys
import time
import psycopg2
from psycopg2 import sql
from typing import Optional

class DatabaseInitializer:
    def __init__(self, host: str, port: int, database: str, username: str, password: str, max_retries: int = 30):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.max_retries = max_retries
        self.conn = None

    def connect(self) -> bool:
        """데이터베이스 연결 시도 (재시도 로직 포함)"""
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.username,
                    password=self.password,
                    connect_timeout=5
                )
                self.conn.autocommit = True
                print(f"✓ Database connected: {self.host}:{self.port}/{self.database}")
                return True
            except psycopg2.OperationalError as e:
                retry_count += 1
                if retry_count >= self.max_retries:
                    print(f"✗ Failed to connect after {self.max_retries} attempts")
                    print(f"  Error: {e}")
                    return False
                wait_time = min(5, retry_count)
                print(f"⏳ Connection attempt {retry_count}/{self.max_retries} failed. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            except Exception as e:
                print(f"✗ Connection error: {e}")
                return False
        return False

    def create_database_and_user(self, user_index: int) -> bool:
        """데이터베이스와 사용자 생성"""
        if not self.conn:
            print("✗ Database connection not established")
            return False

        user_name = f"user_{user_index:02d}"
        db_name = f"db_{user_index:02d}"
        user_password = f"pw_{user_index:02d}"

        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
                if cursor.fetchone():
                    print(f"  ℹ Database {db_name} already exists, skipping creation")
                else:
                    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                    print(f"  ✓ Database {db_name} created")

                cursor.execute(
                    sql.SQL("CREATE USER {} WITH PASSWORD %s").format(sql.Identifier(user_name)),
                    (user_password,)
                )
                cursor.execute(
                    sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
                        sql.Identifier(db_name),
                        sql.Identifier(user_name)
                    )
                )
                cursor.execute(
                    sql.SQL("GRANT ALL ON SCHEMA public TO {}").format(sql.Identifier(user_name))
                )
                cursor.execute(
                    sql.SQL("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO {}").format(
                        sql.Identifier(user_name)
                    )
                )
                print(f"  ✓ User {user_name} created with database {db_name}")

            self.create_tables_in_database(db_name, user_name)
            return True

        except psycopg2.Error as e:
            print(f"  ✗ Error creating database/user: {e}")
            return False

    def create_tables_in_database(self, db_name: str, user_name: str) -> bool:
        """새로운 데이터베이스에서 테이블 생성"""
        db_conn = None
        try:
            db_conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=db_name,
                user=self.username,
                password=self.password
            )
            db_conn.autocommit = True

            with db_conn.cursor() as cursor:
                cursor.execute(
                    sql.SQL("GRANT ALL ON SCHEMA public TO {}").format(sql.Identifier(user_name))
                )
                cursor.execute(
                    sql.SQL("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO {}").format(
                        sql.Identifier(user_name)
                    )
                )

                cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                print(f"  ✓ Vector extension installed")

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS documents (
                        id SERIAL PRIMARY KEY,
                        content TEXT NOT NULL,
                        embedding vector(1536),
                        metadata JSONB,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                print(f"  ✓ Table documents created")

                cursor.execute(
                    sql.SQL("GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO {}").format(
                        sql.Identifier(user_name)
                    )
                )

                cursor.execute('''
                    CREATE INDEX IF NOT EXISTS idx_documents_created_at ON documents(created_at DESC);
                ''')
                print(f"  ✓ Indexes created")

            print(f"✓ Database {db_name} initialized successfully")
            return True

        except psycopg2.Error as e:
            print(f"✗ Error initializing database {db_name}: {e}")
            return False
        finally:
            if db_conn:
                db_conn.close()

    def initialize(self, num_users: int = 2) -> bool:
        """전체 초기화 프로세스 실행"""
        if not self.connect():
            return False

        print(f"\n📋 Creating {num_users} database(s) and user(s)...")
        success = True
        for i in range(0, num_users + 1):
            print(f"\n[{i}/{num_users}] User {i:02d}")
            if not self.create_database_and_user(i):
                success = False

        if self.conn:
            self.conn.close()

        if success:
            print("\n✓ Database initialization completed successfully!")
        else:
            print("\n✗ Database initialization completed with errors")

        return success

def main():
    parser = argparse.ArgumentParser(
        description="PostgreSQL RDS 데이터베이스 초기화 스크립트",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Terraform에서 자동으로 호출:
  python3 init_database.py --host rds.amazonaws.com --port 5432 --database nxtcloud_db --username postgres --password secret

  # 수동 실행:
  python3 init_database.py \\
    --host localhost \\
    --port 5432 \\
    --database test_db \\
    --username postgres \\
    --password mypassword \\
    --num-users 3
        """
    )

    parser.add_argument("--host", required=True, help="RDS endpoint hostname")
    parser.add_argument("--port", type=int, default=5432, help="RDS port (default: 5432)")
    parser.add_argument("--database", required=True, help="Initial database name")
    parser.add_argument("--username", required=True, help="Master username")
    parser.add_argument("--password", required=True, help="Master password")
    parser.add_argument("--num-users", type=int, default=2, help="Number of users/databases to create (default: 2)")
    parser.add_argument("--max-retries", type=int, default=30, help="Max connection retry attempts (default: 30)")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("PostgreSQL RDS Database Initialization")
    print("="*60)
    print(f"Host:     {args.host}")
    print(f"Port:     {args.port}")
    print(f"Database: {args.database}")
    print(f"Username: {args.username}")
    print("="*60 + "\n")

    initializer = DatabaseInitializer(
        host=args.host,
        port=args.port,
        database=args.database,
        username=args.username,
        password=args.password,
        max_retries=args.max_retries
    )

    success = initializer.initialize(num_users=args.num_users)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
