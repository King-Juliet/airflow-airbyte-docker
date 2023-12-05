-- model for product performance analytics

SELECT date,
    {{ref('stg_product')}}.product_id,
    product_name,
    quantity,
    selling_price
    FROM {{ref('stg_product')}}
    LEFT JOIN {{ref('stg_carts')}} 
    ON {{ref('stg_product')}}.product_id = {{ref('stg_carts')}}.product_id