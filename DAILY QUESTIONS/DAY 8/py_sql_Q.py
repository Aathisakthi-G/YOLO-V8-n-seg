# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def second_largest(lst):
    unique_numbers = list(set(lst))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

print(second_largest([10, 20, 4, 45, 99, 99]))  # Output: 45


#2
def primes_in_range(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

print(primes_in_range(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#3
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False


#4
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120 (1*2*3*4*5)


#5
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)


#SQL

#1
SELECT department, employee_name, salary
FROM employees e1
WHERE salary = (SELECT MAX(salary) FROM employees e2 WHERE e1.department = e2.department);

#2
SELECT * FROM orders
ORDER BY order_date ASC
LIMIT 5;


#3
SELECT DISTINCT customer_id 
FROM orders 
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);


#4
1. INNER JOIN
Description: Returns only the records that have matching values in both tables.
Example SQL Query:
"SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;"
Retrieves only the orders that have a matching customer in the customers table.
2. LEFT JOIN
Description: Returns all records from the left table and the matching records from the right table. If no match is found, NULL values are returned for the right table’s columns.
Example SQL Query:
"SELECT * FROM orders LEFT JOIN customers ON orders.customer_id = customers.id;"
Retrieves all orders, including those without a matching customer.
3. RIGHT JOIN
Description: Returns all records from the right table and the matching records from the left table. If no match is found, NULL values are returned for the left table’s columns.
Example SQL Query:
"SELECT * FROM orders RIGHT JOIN customers ON orders.customer_id = customers.id;"
Retrieves all customers, including those who haven’t placed any orders.
4. FULL JOIN
Description: Returns all records from both tables. If there’s no match, NULL values are returned for missing data from either table.
Example SQL Query:
"SELECT * FROM orders FULL JOIN customers ON orders.customer_id = customers.id;"
Retrieves all orders and all customers, even if they don’t have matching records.

#5
SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(amount) AS total_revenue
FROM sales
GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY month;


