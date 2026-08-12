# Data Lineage

Customer:
Operational source -> raw/customer -> curated/customer -> dim_customer -> analytics

Policy:
Policy source -> raw/policy -> curated/policy -> dim_policy -> fact_claim relationship -> analytics

Claims:
Claims source -> raw/claims -> curated/claims -> fact_claim -> analytics
