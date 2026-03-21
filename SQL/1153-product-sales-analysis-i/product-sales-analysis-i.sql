# Write your MySQL query statement below
select product_name,year,price 
from Sales s JOIN Product p ON s.product_id = p.product_id
ORDER by s.sale_id;
