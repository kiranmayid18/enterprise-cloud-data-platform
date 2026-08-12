output "raw_bucket" {
  value = aws_s3_bucket.raw.bucket
}

output "curated_bucket" {
  value = aws_s3_bucket.curated.bucket
}

output "ingestion_queue_url" {
  value = aws_sqs_queue.ingestion.url
}

output "alerts_topic_arn" {
  value = aws_sns_topic.alerts.arn
}
