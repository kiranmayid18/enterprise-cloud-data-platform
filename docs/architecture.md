# Technical Architecture

## Design Principles
- Separate raw, curated, and warehouse layers.
- Use incremental processing wherever practical.
- Keep ingestion decoupled from processing.
- Make retries idempotent.
- Treat data quality as part of the pipeline.
- Use version-controlled deployments and peer review.
- Monitor technical health and business-data health separately.

## AWS Mapping
- S3: raw and curated object storage
- SQS: ingestion buffering and retry decoupling
- SNS: operational alerting
- EC2: long-running processing where appropriate
- Auto Scaling: variable compute demand
- VPC: network isolation
- EBS: persistent EC2 block storage
- ELB: service/API ingestion components

## Azure Mapping
- Azure Data Factory: orchestration
- ADLS Gen2: raw and curated storage
- Azure SQL / Synapse / Fabric Warehouse: serving
- Databricks: Spark transformations
- Azure Monitor / Log Analytics: observability
- Key Vault: secrets
- Purview: cataloguing and lineage
