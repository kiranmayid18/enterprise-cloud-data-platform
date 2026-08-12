-- Generic SCD Type 2 pattern.

UPDATE dim_customer d
SET effective_to = CURRENT_DATE,
    is_current = 0
WHERE d.is_current = 1
  AND EXISTS (
      SELECT 1
      FROM stg_customer s
      WHERE s.customer_id = d.customer_id
        AND (
             s.customer_name <> d.customer_name
          OR s.country <> d.country
        )
  );

INSERT INTO dim_customer (
    customer_key,
    customer_id,
    customer_name,
    country,
    effective_from,
    effective_to,
    is_current
)
SELECT
    ROW_NUMBER() OVER (ORDER BY s.customer_id) + 1000,
    s.customer_id,
    s.customer_name,
    s.country,
    CURRENT_DATE,
    NULL,
    1
FROM stg_customer s
LEFT JOIN dim_customer d
  ON s.customer_id = d.customer_id
 AND d.is_current = 1
WHERE d.customer_id IS NULL
   OR s.customer_name <> d.customer_name
   OR s.country <> d.country;
