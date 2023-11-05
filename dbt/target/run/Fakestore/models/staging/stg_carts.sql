
  create view "Fakestore"."public"."stg_carts__dbt_tmp"
    
    
  as (
    SELECT cart_id AS cart_id,
    user_id AS user_id,
    Date AS date,
    product_id AS product_id,
    Quantity AS quantity
FROM "Fakestore"."public"."carts"
  );