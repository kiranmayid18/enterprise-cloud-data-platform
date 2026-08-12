# Enterprise Cloud Data Platform

A portfolio implementation of an enterprise data platform for insurance claims, policy, and reporting data.

> **Portfolio disclaimer:** This repository is a technical demonstration based on enterprise data-engineering patterns and the author's hands-on experience. It does not contain confidential client code, production credentials, or proprietary datasets.

## Project Goals

This project demonstrates:
- batch and incremental ingestion;
- metadata-driven processing;
- SQL and Python/PySpark transformations;
- dimensional warehouse modelling;
- SCD Type 1 and Type 2;
- data-quality and reconciliation controls;
- lineage and governance documentation;
- CI/CD and automated testing;
- Infrastructure as Code;
- monitoring and incident-response patterns;
- cloud scalability, reliability, and cost considerations.

## Business Scenario

An insurance organisation receives customer, policy, and claims data from operational systems. The platform validates, incrementally processes, transforms, reconciles, and prepares trusted warehouse datasets for reporting and analytics.

## High-Level Architecture

```text
Operational DB / Files / REST APIs
              |
              v
      Cloud Landing / Raw Zone
        (S3 / ADLS Gen2)
              |
        Metadata / Watermark
              |
              v
      Orchestration Layer
       (ADF-style pattern)
              |
       +------+------+
       |             |
       v             v
 Python/PySpark    SQL ELT
 Transformations  Transformations
       |             |
       +------+------+
              |
              v
      Curated / Conformed Zone
              |
              v
      Enterprise Warehouse
   Dimensions + Fact Tables
              |
       +------+------+
       |             |
       v             v
 Analytics/BI     Data Quality
                   Monitoring
```

## Cloud & Platform Coverage

### AWS
Amazon S3, EC2, VPC, SQS, SNS, EBS, ELB, and Auto Scaling patterns.

### Azure
Azure Data Factory, ADLS Gen2, Azure SQL, Databricks, Synapse, Fabric, Azure Monitor, Log Analytics, Key Vault, and Purview concepts.

## Repository Structure

```text
.github/workflows/ci.yml
config/pipeline_config.json
docs/
sample_data/
scripts/
sql/
src/
terraform/
tests/
README.md
requirements.txt
```

## Engineering Practices Demonstrated

### Data Development & Integration
ETL/ELT, metadata-driven processing, reusable patterns, incremental/delta loading, file/API/database ingestion.

### SQL & Data Warehousing
Star schema, fact and dimension tables, SCD Type 2, CTE/window-function patterns, reconciliation, data validation.

### Python & PySpark Concepts
Python transformations and validation with patterns that can be moved to Databricks/PySpark for larger workloads.

### CI/CD
GitHub Actions performs Python compilation and automated tests on pushes and pull requests. The same principles map to Jenkins and Azure DevOps.

### Data Quality & Observability
Mandatory fields, duplicates, referential integrity, numeric/date validation, reconciliation, failure thresholds, runbooks.

### Governance & Lineage
Source ownership, raw-to-curated-to-warehouse lineage, classification, quality ownership, and access principles.

## Run Locally

```bash
python -m venv .venv
pip install -r requirements.txt
python -m src.pipeline
python -m pytest -q
```

## Scalability & Cost Considerations

- partition large datasets by date/domain;
- use watermark processing instead of full reloads;
- decouple ingestion and processing using queues;
- use autoscaling for variable compute demand;
- monitor storage and compute growth;
- archive aged data with lifecycle policies;
- avoid repeated full-table scans;
- use idempotent retry-safe processing.

## Lead Data Engineering Responsibilities Represented

- defining modelling and ingestion standards;
- setting quality gates;
- establishing CI/CD and review expectations;
- documenting technical architecture;
- designing escalation and runbook processes;
- balancing scalability, reliability, and cost;
- translating business requirements into engineering solutions.

## Author

**Kiranmayi Dodda**  
GitHub: https://github.com/kiranmayid18
