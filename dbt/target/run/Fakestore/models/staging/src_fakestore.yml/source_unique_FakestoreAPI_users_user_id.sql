select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    user_id as unique_field,
    count(*) as n_records

from "Fakestore"."public"."users"
where user_id is not null
group by user_id
having count(*) > 1



      
    ) dbt_internal_test