-- model for user shopping habits

SELECT 
    {{ref('stg_users')}}.user_id,
    {{ref('stg_product')}}.product_id,
    {{ref('stg_product')}}.product_name,
    COUNT(cart_id) AS total_carts,
    SUM(Quantity) AS total_quantity,
    SUM(selling_price) AS total_amount,
    {{ref('stg_users')}}.city
FROM {{ref('stg_product')}}
LEFT JOIN {{ref('stg_carts')}} ON {{ref('stg_product')}}.product_id = {{ref('stg_carts')}}.product_id
LEFT JOIN {{ref('stg_users')}} ON {{ref('stg_carts')}}.user_id = {{ref('stg_users')}}.user_id
GROUP BY {{ref('stg_product')}}.product_id, {{ref('stg_users')}}.user_id, product_name, {{ref('stg_users')}}.city
ORDER BY total_quantity, total_amount
