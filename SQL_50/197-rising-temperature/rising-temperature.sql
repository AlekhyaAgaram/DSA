# Write your MySQL query statement below

/*
have to do self joing on weather table
can not subtract 1 from date so hv to use datediff function
*/

select w1.id from Weather w1 JOIN weather w2 
on datediff(w1.recordDate,w2.recordDate) = 1
where w1.temperature > w2.temperature;