-- Write your PostgreSQL query statement below
select v.customer_id, COUNT(*) as "count_no_trans"
from Visits as v
left join Transactions as t
using (visit_id)
where t.transaction_id is null
group by v.customer_id;