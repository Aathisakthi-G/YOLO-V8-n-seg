# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120

#2
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]


#3
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False


#4
lst = [1, 2, 3]
lst.append(4)  # Allowed
print(lst)  # Output: [1, 2, 3, 4]

s = "hello"
s[0] = 'H'  # Error: Strings are immutable

#5
from collections import Counter

def char_frequency(s):
    return Counter(s)

print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


#SQL

#1
SELECT employee_name, department, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);

#2
SELECT * 
FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY id DESC) AS row_num
    FROM orders
) subquery
WHERE row_num <= 5;


#3
SELECT * 
FROM orders 
WHERE order_date >= CURRENT_DATE - INTERVAL '7' DAY;


#4
SELECT category, SUM(sales_amount) AS total_sales
FROM ecommerce_sales
GROUP BY category;

#5
DELETE FROM sales
WHERE id NOT IN (
    SELECT MAX(id)
    FROM sales
    GROUP BY customer_id, product_id, order_date
);

