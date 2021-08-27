
WITH top_selling_tickets
AS (SELECT 
       event_name,
       ROW_NUMBER() OVER (
          ORDER BY num_tickets DESC) row_num
    FROM 
       ticket_sales
   )
SELECT 
   event_name
FROM 
   top_selling_tickets
WHERE 
   row_num <= 3;