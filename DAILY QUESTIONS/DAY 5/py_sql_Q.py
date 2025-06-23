# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def are_rotations(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

print(are_rotations("hello", "lohel"))  # True
print(are_rotations("abc", "bca"))      # True
print(are_rotations("abc", "acb"))      # False

#2
from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  # Output: 3


#3
def sum_of_squares(lst):
    return sum(x**2 for x in lst)

print(sum_of_squares([1, 2, 3]))  # Output: 14 (1^2 + 2^2 + 3^2)


#4
from itertools import combinations, permutations

items = [1, 2, 3]
print(list(combinations(items, 2)))  # [(1,2), (1,3), (2,3)]
print(list(permutations(items, 2)))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

#5
def has_unique_chars(s):
    return len(set(s)) == len(s)

print(has_unique_chars("abcdef"))  # True
print(has_unique_chars("aabbcc"))  # False


#SQL

#1
SELECT department, employee_name, salary
FROM (
    SELECT department, employee_name, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
) ranked
WHERE rank <= 3;


#2
SELECT YEAR(order_date) AS year, SUM(total_amount) AS total_revenue
FROM sales
GROUP BY YEAR(order_date)
ORDER BY year;


#3
SELECT customer_id, COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;


#4
SELECT product_id, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_id
HAVING SUM(sales_amount) > 10000;


#5
SELECT employee_id, employee_name
FROM employees
WHERE manager_id IS NULL;

