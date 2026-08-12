CREATE TABLE dim_customer (
    customer_key INTEGER PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(200) NOT NULL,
    country VARCHAR(50),
    effective_from DATE NOT NULL,
    effective_to DATE,
    is_current INTEGER NOT NULL
);

CREATE TABLE dim_policy (
    policy_key INTEGER PRIMARY KEY,
    policy_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    policy_type VARCHAR(50),
    start_date DATE,
    status VARCHAR(50)
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE NOT NULL,
    calendar_year INTEGER NOT NULL,
    calendar_month INTEGER NOT NULL,
    calendar_day INTEGER NOT NULL
);
