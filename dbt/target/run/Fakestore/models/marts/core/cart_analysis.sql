
  create view "Fakestore"."public"."cart_analysis__dbt_tmp"
    
    
  as (
    SELECT date,
    user_id,
    cart_id
FROM "Fakestore"."public"."stg_carts"
WHERE quantity = 0
  );