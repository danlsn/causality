--Select Messages I've Sent Grouped By Date
select date(message.date / 1000000000 + strftime("%s", "2001-01-01"), "unixepoch", "localtime") date_time,
       count(ROWID)                                                                             count
from message
where message.is_from_me = 1
group by date_time
order by count desc
limit 10;

--Select Messages I've Sent Grouped by Year
select strftime("%Y",
                date(message.date / 1000000000 + strftime("%s", "2001-01-01"), "unixepoch", "localtime")) date_time,
       count(ROWID)                                                                                       count
from message
where message.is_from_me = 1
group by date_time
order by date_time desc;