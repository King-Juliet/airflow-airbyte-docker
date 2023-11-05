
  create view "Fakestore"."public"."stg_product__dbt_tmp"
    
    
  as (
    SELECT Product_id AS product_id,
       Name AS product_name,
       CAST(price AS INTEGER) AS selling_price
       FROM "Fakestore"."public"."products"
  );