CREATE TABLE stg_customer (
    customer_id VARCHAR(50),
    customer_name VARCHAR(200),
    country VARCHAR(50),
    modified_date DATE
);

CREATE TABLE stg_policy (
    policy_id VARCHAR(50),
    customer_id VARCHAR(50),
    policy_type VARCHAR(50),
    start_date DATE,
    status VARCHAR(50),
    modified_date DATE
);

CREATE TABLE stg_claim (
    claim_id VARCHAR(50),
    policy_id VARCHAR(50),
    claim_date DATE,
    claim_amount DECIMAL(14,2),
    claim_status VARCHAR(50),
    modified_date DATE
);
