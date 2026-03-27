# Write your MySQL query statement below
select A.machine_id , ROUND(AVG(B.timestamp - A.timestamp),3) as processing_time 
from Activity A join Activity B on A.process_id = B.process_id and A.machine_id = B.machine_id 
where  A.activity_type = 'start' and B.activity_type = 'end'
group by machine_id;
