CREATE TABLE fact_claim (
    claim_key INTEGER PRIMARY KEY,
    claim_id VARCHAR(50) NOT NULL,
    policy_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,
    claim_amount DECIMAL(14,2) NOT NULL,
    claim_status VARCHAR(50),
    FOREIGN KEY (policy_key) REFERENCES dim_policy(policy_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);
