# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
import math
def find_gcd(a, b):
    return math.gcd(a, b)

print(find_gcd(48, 18))  # Output: 6

#2
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

nested = [[1, 2, [3, 4]], 5, [6, 7]]
print(flatten_list(nested))  # Output: [1, 2, 3, 4, 5, 6, 7]

#3
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))  # Output: [1, 2, 3, 4, 5]

#4
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

combined = list(zip(names, scores))
print(combined)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

#5
import math
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

print(is_perfect_square(25))  # Output: True
print(is_perfect_square(26))  # Output: False


#SQL

#1
SELECT product_id
FROM sales
GROUP BY product_id
ORDER BY COUNT(*) DESC
LIMIT 1 OFFSET 1;

#2
SELECT product_id, sale_date, amount,SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) AS cumulative_sales
FROM sales;

#3
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
    AND s.sale_date >= CURRENT_DATE - INTERVAL '30 days'
WHERE s.customer_id IS NULL;

#4
SELECT customer_id, 
       total_spent,
       CASE 
           WHEN total_spent > 1000 THEN 'Premium'
           WHEN total_spent BETWEEN 500 AND 1000 THEN 'Gold'
           ELSE 'Regular'
       END AS customer_category
FROM (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM sales
    GROUP BY customer_id
) AS customer_spending;


#5
SELECT customer_id, COUNT(order_id) AS total_orders
FROM sales
GROUP BY customer_id
ORDER BY total_orders DESC;
