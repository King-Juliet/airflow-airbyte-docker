-- model to view carts that are empty for a given user for a given day

SELECT date,
    user_id,
    cart_id
FROM {{ref('stg_carts')}}
WHERE quantity = 0