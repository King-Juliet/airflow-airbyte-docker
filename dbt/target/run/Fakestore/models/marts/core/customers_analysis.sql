
  create view "Fakestore"."public"."customers_analysis__dbt_tmp"
    
    
  as (
    SELECT 
    "Fakestore"."public"."stg_users".user_id,
    "Fakestore"."public"."stg_product".product_id,
    "Fakestore"."public"."stg_product".product_name,
    COUNT(cart_id) AS total_carts,
    SUM(Quantity) AS total_quantity,
    SUM(selling_price) AS total_amount,
    "Fakestore"."public"."stg_users".city
FROM "Fakestore"."public"."stg_product"
LEFT JOIN "Fakestore"."public"."stg_carts" ON "Fakestore"."public"."stg_product".product_id = "Fakestore"."public"."stg_carts".product_id
LEFT JOIN "Fakestore"."public"."stg_users" ON "Fakestore"."public"."stg_carts".user_id = "Fakestore"."public"."stg_users".user_id
GROUP BY "Fakestore"."public"."stg_product".product_id, "Fakestore"."public"."stg_users".user_id, product_name, "Fakestore"."public"."stg_users".city
ORDER BY total_quantity, total_amount
  );