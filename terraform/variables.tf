variable "aws_region" {
  type    = string
  default = "eu-west-2"
}

variable "project_name" {
  type    = string
  default = "enterprise-data-platform"
}

variable "raw_bucket_name" {
  type    = string
  default = "replace-with-unique-raw-bucket-name"
}

variable "curated_bucket_name" {
  type    = string
  default = "replace-with-unique-curated-bucket-name"
}
