terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

resource "aws_db_instance" "postgres" {
  identifier     = var.db_instance_identifier
  engine         = "postgres"
  engine_version = var.postgres_version
  instance_class = var.instance_class

  allocated_storage = var.allocated_storage
  storage_type      = "gp3"
  storage_encrypted = true

  db_name  = var.database_name
  username = var.db_master_username
  password = var.db_master_password

  db_subnet_group_name   = aws_db_subnet_group.postgres.name
  parameter_group_name   = aws_db_parameter_group.postgres.name
  vpc_security_group_ids = [aws_security_group.postgres.id]

  publicly_accessible             = true
  skip_final_snapshot             = true
  enabled_cloudwatch_logs_exports = []
  performance_insights_enabled    = false

  provisioner "local-exec" {
    command = <<-EOT
      python3 -m venv venv
      source venv/bin/activate
      pip install psycopg2-binary python-dotenv
      python3 init_database.py \
        --host=${self.address} \
        --port=${self.port} \
        --database=${var.database_name} \
        --username=${var.db_master_username} \
        --password=${var.db_master_password}
      deactivate
      rm -rf venv
    EOT
    interpreter = ["/bin/bash", "-c"]
  }
}

resource "aws_db_subnet_group" "postgres" {
  name       = "${var.db_instance_identifier}-subnet-group"
  subnet_ids = data.aws_subnets.default.ids
}

resource "aws_db_parameter_group" "postgres" {
  name   = "${var.db_instance_identifier}-params"
  family = "postgres${var.postgres_family_version}"
}

resource "aws_security_group" "postgres" {
  name        = "${var.db_instance_identifier}-sg"
  description = "Security group for PostgreSQL RDS"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
