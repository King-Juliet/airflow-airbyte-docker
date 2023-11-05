SELECT date,
    user_id,
    cart_id
FROM {{ref('stg_carts')}}
WHERE quantity = 0