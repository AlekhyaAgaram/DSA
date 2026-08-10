# Write your MySQL query statement below
SELECT e.name, b.bonus 
FROM Employee e LEFT OUTER JOIN bonus b
ON e.empId = b.empId
WHERE b.bonus IS null or b.bonus < 1000; 