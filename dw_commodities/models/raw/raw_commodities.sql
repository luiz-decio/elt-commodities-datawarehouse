with source as (
    select
        "Date",
        "Close",
        symbol
    from {{ source ('dw_sales', 'commodities')}}
),

renamed as (
    select
        cast("Date" as date) as date,
        "Close" as closing_price,
        symbol
    from source
)

select * from renamed