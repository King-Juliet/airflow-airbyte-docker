-- Light data transformation performed: column name change

SELECT cart_id AS cart_id,
    user_id AS user_id,
    Date AS date,
    product_id AS product_id,
    Quantity AS quantity
FROM {{source('FakestoreAPI', 'carts')}}