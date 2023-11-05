SELECT date,
    user_id,
    cart_id
FROM "Fakestore"."public"."stg_carts"
WHERE quantity = 0