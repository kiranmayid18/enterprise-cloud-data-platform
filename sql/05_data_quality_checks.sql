SELECT * FROM stg_claim
WHERE claim_id IS NULL OR policy_id IS NULL OR claim_date IS NULL;

SELECT claim_id, COUNT(*) AS duplicate_count
FROM stg_claim
GROUP BY claim_id
HAVING COUNT(*) > 1;

SELECT * FROM stg_claim
WHERE claim_amount < 0;

SELECT c.*
FROM stg_claim c
LEFT JOIN stg_policy p ON c.policy_id = p.policy_id
WHERE p.policy_id IS NULL;
