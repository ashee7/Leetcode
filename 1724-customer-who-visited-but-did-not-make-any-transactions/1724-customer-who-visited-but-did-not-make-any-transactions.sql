# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans
    from Visits a left join Transactions b 
        on a.visit_id = b.visit_id
    where b.transaction_id is Null 
    group by customer_id;