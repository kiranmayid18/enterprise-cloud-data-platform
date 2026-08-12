# Data Governance

## Ownership
Each source should have a named business owner and technical owner.

## Classification
Examples:
- customer identifiers: confidential
- policy identifiers: internal/confidential
- claim amounts: confidential
- operational metadata: internal

## Quality Controls
Document rule name, dataset, threshold, owner, alerting path, and remediation process.

## Access
Use least privilege. Reporting users should not have direct write access to production datasets.

## Metadata & Lineage
Capture source system, ingestion timestamp, transformation stage, target object, owner, and quality status.
