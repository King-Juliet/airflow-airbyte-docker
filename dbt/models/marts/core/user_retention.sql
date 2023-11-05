SELECT user_id,
    MIN(date) AS first_purchase_date,
    MAX(date) AS last_purchase_date
FROM {{ref('stg_carts')}}
GROUP BY user_id
