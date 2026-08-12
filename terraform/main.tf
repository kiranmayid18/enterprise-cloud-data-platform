terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "raw" {
  bucket = var.raw_bucket_name
}

resource "aws_s3_bucket" "curated" {
  bucket = var.curated_bucket_name
}

resource "aws_sqs_queue" "ingestion" {
  name                       = "${var.project_name}-ingestion"
  visibility_timeout_seconds = 60
}

resource "aws_sns_topic" "alerts" {
  name = "${var.project_name}-alerts"
}

resource "aws_vpc" "data_platform" {
  cidr_block           = "10.20.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "${var.project_name}-vpc"
  }
}
