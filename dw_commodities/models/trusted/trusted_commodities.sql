-- models/trusted/trusted_commodities.sql

with commodities as (
    select
        date,
        symbol,
        closing_price
    from 
        {{ ref ('raw_commodities') }}
),

transactions as (
    select
        date,
        symbol,
        action,
        quantity
    from 
        {{ ref ('raw_commodities_sell') }}
),

joined as (
    select
        c.date,
        c.symbol,
        c.closing_price,
        t.action,
        t.quantity,
        (t.quantity * c.closing_price) as value,
        case
            when t.action = 'sell' then (t.quantity * c.closing_price)
            else -(t.quantity * c.closing_price)
        end as balance
    from
        commodities c
    inner join
        transactions t
    on
        c.date = t.date
        and c.symbol = t.symbol
),

last_day as (
    select
        max(date) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        date = (select max_date from last_day)
)

select
    date,
    symbol,
    closing_price,
    action,
    quantity,
    value,
    balance
from
    filtered