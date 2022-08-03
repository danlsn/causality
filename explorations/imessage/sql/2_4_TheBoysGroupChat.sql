--How Many Messages Sent in 'The Boys' Group Chat?

--Select ROWID for the Group Chat
select ROWID, display_name
from chat
where display_name like 'The Boys';

--Select Count of All Messages with the right chat_id
select count(*) count
from chat_message_join
where chat_id = (select ROWID from chat where display_name like 'The Boys');

--Join Chat and Message Tables by chat_message_join, group by display_name
select display_name, count(*) count
from chat
         join chat_message_join cmj on chat.ROWID = cmj.chat_id
         join message m on cmj.message_id = m.ROWID
where display_name not like ""
group by display_name
order by count desc;