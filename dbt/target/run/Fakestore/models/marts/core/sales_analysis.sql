
  create view "Fakestore"."public"."sales_analysis__dbt_tmp"
    
    
  as (
    SELECT date,
    "Fakestore"."public"."stg_product".product_id,
    product_name,
    quantity,
    selling_price
    FROM "Fakestore"."public"."stg_product"
    LEFT JOIN "Fakestore"."public"."stg_carts" 
    ON "Fakestore"."public"."stg_product".product_id = "Fakestore"."public"."stg_carts".product_id
  );