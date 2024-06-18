with source as (
    select
        date,
        symbol,
        action,
        quantity
    from {{ source ('dw_sales', 'commodities_sell')}}
),

renamed as (
    select
        cast(date as date) as date,
        symbol,
        action,
        cast(quantity as int) as quantity
    from source
)

select * from renamed