-- How many days were there where the number of tickets sold was less than 25% of the mean?
-- Hint: first find the daily mean by calculating daily number of sales
WITH sales_per_day AS (
    -- Get the number of sales per day
    SELECT
        d.caldate as day,
        sum(qtysold) AS num_sales
    FROM sales
             join date d on sales.dateid = d.dateid
    GROUP BY d.dateid
),


     dsa AS (
         -- Get the mean number of sales per day
         SELECT AVG(num_sales)   as daily_sales_avg
         FROM sales_per_day
     )
SELECT  count(*)
FROM dsa
         JOIN sales_per_day spd
              ON spd.num_sales < 0.25 * dsa.daily_sales_avg
;

-- 2.) What was the percent change in orders between September 9 & 10?
/* Get the day-over-day change in sales. */
WITH sales_per_day AS (
    -- Each row contains the number of sales for a given day
    SELECT
        d.caldate as day,
        COUNT(*) AS num_sales
    FROM sales
             join date d on d.dateid = sales.dateid
    GROUP BY d.dateid
),


     curr_day_and_prev_day_sales AS (
         -- Each row contains the current day and previous day's sales
         -- Note that this answers the question, the last step we add is a bonus
         SELECT
             day,

             num_sales AS curr_day_sales,
             LAG(num_sales, 1) OVER (ORDER BY day) AS prev_day_sales
         FROM sales_per_day
     )

SELECT
    ROUND(100.0 * (curr_day_sales - prev_day_sales) / prev_day_sales,1) AS pct_change
FROM curr_day_and_prev_day_sales
where day = '2008-09-10'
-- ORDER BY day DESC
;

-- 4.) What was the top event in Los Angeles?
-- Note: Here top event means in terms of the overall price paid, i.e.: the one with the most money spent in aggregate in tickets.
with la_events as (
    select v.venueid, v.venuename, ev.eventid, ev.eventname from event ev
        join venue v on ev.venueid = v.venueid
        where v.venuecity = 'Los Angeles'

),
   la_grosses as (
    select sales.eventid, sum(sales.pricepaid) as gross_sales from  sales join la_events on la_events.eventid =sales.eventid
                                               group by sales.eventid
)

select la_events.eventname, la_grosses.gross_sales from  la_events join la_grosses
    on la_events.eventid = la_grosses.eventid
    group by la_events.eventname
    order by  gross_sales desc
 limit 1;
;

-- Bonus question: what was the most recent event in each city?
select max(ev.dateid), ev.eventid, ev.eventname, v.venuecity, d.caldate as day
from event ev
join venue v on v.venueid = ev.venueid
join date d on d.dateid = ev.dateid
group by v.venuecity;

-- What city had the most events?
select count(ev.eventid) as number_of_events, v.venuecity
from event ev
join venue v on v.venueid = ev.venueid
group by v.venuecity
order by number_of_events desc
limit 1;

-- How many users have bought a ticket to the category called 'Musicals'?
WITH musicals as (
  select distinct ev.eventid, ev.eventname from category cat join main.event ev on cat.catid = ev.catid and  cat.catname = 'Musicals'
) select count(distinct buyerid) from musicals join sales on sales.eventid = musicals.eventid;


-- How many tickets were sold by resellers (someone who bought tickets for an event and later sold tickets to that same event)?
select sum(s2.qtysold) from sales s1 join sales s2 on s1.buyerid = s2.sellerid and s1.eventid = s2.eventid
AND s2.saletime > s1.saletime
;


-- 7.) Which holiday had the most ticket sales?
-- Ambiguity: does this mean which day the sale occurs or which day the event occurs?
-- Sale
WITH HOLIDAYS as (
    select dateid, caldate as day from date d where holiday = 1
) select holidays.day, sum(s.qtysold) tickets_sold from holidays
    join sales s on HOLIDAYS.dateid = s.dateid
    join date d on d.dateid = s.dateid
    group by s.dateid
    order by tickets_sold desc
    limit 1;

select day from (
select d.caldate as day, sum(s.qtysold) tickets_sold from sales s
    join date d on d.dateid = s.dateid and d.holiday = 1
    group by s.dateid
    order by tickets_sold desc
    limit 1

);

-- How many buyer pairs have attended three or more events together?
-- In other words, how many users have bought tickets to the same event three or more times?
-- Hierarchical query? No, group by two columns.
select count(*)
from (SELECT s1.buyerid                 AS buyer_a,
             s2.buyerid                 AS buyer_b,
             COUNT(DISTINCT s1.eventid) AS num_events_attended_together
      FROM sales s1
               JOIN sales s2
                    ON s2.eventid = s1.eventid
                        AND s2.buyerid > s1.buyerid
--     	where  buyer_a  = 3451

      GROUP BY buyer_a, buyer_b
      having num_events_attended_together > 2
      order by num_events_attended_together desc
      ) babbneat;
-- ,     	  buyer_b;

-- How many users have bought tickets to an out-of-state event?
-- with event_states as (
--     select distinct ev.eventid, ev.eventname, v.venuename, v.venuestate
-- --               v.venuestate
-- from event ev
--          join venue v on v.venueid = ev.venueid
-- )

-- ), oos_purchases as (
--
--
--
-- )
-- select count(distinct userid)
-- with event_states as (
--     select distinct ev.eventid, ev.eventname, v.venuename, v.venuestate
-- --               v.venuestate
-- from event ev
--          join venue v on v.venueid = ev.venueid
-- )
-- select count(distinct user)
SELECT COUNT(DISTINCT u.userid)
	  FROM sales s
	  JOIN users u ON u.userid = s.buyerid
	  JOIN event e ON e.eventid = s.eventid
	  JOIN venue v ON v.venueid = e.venueid
      where v.venuestate != u.state
	;

-- 10.) Find the top 3 cities for sales. (Either by number of tickets sold or gross revenue).
-- Also, the city where the venue is or the one where the user lives?
select  v.venuecity, sum(s.qtysold) as total_tickets_sold
	  from sales s
-- 	  join users u on u.userid = s.buyerid
	  join event e on e.eventid = s.eventid
	  join venue v on v.venueid = e.venueid
group by v.venuecity
order by total_tickets_sold desc
limit 3;













