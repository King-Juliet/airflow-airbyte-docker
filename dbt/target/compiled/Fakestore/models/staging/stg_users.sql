SELECT user_id AS user_id,
    username AS user_name,
    Email AS email,
    Phone_number AS phone_number,
    INITCAP(Firstname) || ' ' || INITCAP(Lastname) AS user_fullname,
    INITCAP(City) AS city,
    Number || ' ' || LOWER(street) AS street_address,
    Zipcode AS zipcode,
    Latitude AS latitude,
    Longitude AS Longitude
FROM "Fakestore"."public"."users"