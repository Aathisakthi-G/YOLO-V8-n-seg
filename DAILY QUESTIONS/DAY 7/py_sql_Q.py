# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False

#2
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#3
from collections import Counter

def count_occurrences(lst):
    return dict(Counter(lst))

print(count_occurrences(["apple", "banana", "apple", "orange", "banana"]))
# Output: {'apple': 2, 'banana': 2, 'orange': 1}


#4
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

#5
def find_min_max(lst):
    min_val, max_val = lst[0], lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

print(find_min_max([5, 2, 8, 1, 9, 3]))  # Output: (1, 9)


#SQL

#1
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

#2
SELECT * FROM employees
WHERE salary IS NULL;


#3
SELECT customer_id, COUNT(order_id) AS total_purchases
FROM orders
WHERE order_date >= DATEADD(MONTH, -1, GETDATE())
GROUP BY customer_id
HAVING COUNT(order_id) > 10;

#4
SELECT name, age,
  CASE 
    WHEN age < 18 THEN 'Minor'
    WHEN age BETWEEN 18 AND 65 THEN 'Adult'
    ELSE 'Senior'
  END AS category
FROM customers;

#5
SELECT e.name, e.department, d.department_name
FROM employees e
INNER JOIN departments d ON e.department = d.department_id;

