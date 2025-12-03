-- Write your PostgreSQL query statement below
select unique_id, emp.name as "name"
from EmployeeUNI as e_id
RIGHT JOIN Employees as emp
using (id);