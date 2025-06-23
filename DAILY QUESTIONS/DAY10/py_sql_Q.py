# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def find_unique(lst):
    return list(set(lst))

print(find_unique([1, 2, 2, 3, 4, 4, 5]))

#2
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10, 5

#3
from collections import Counter

def first_non_repeating(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_non_repeating("aabbcddce"))  # Output: e

#4
Difference Between all() and any() Functions in Python
Function

all(): Returns True if all elements in an iterable are True.
any(): Returns True if at least one element in an iterable is True.
Description

all(): Checks if every item in an iterable evaluates to True. If any item is False, the result is False.
any(): Checks if there’s at least one item in the iterable that is True. If all items are False, the result is False.
Example

all(): all([True, True, False]) = False
any(): any([False, False, True]) = True

#5
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]

#SQL

#1
SELECT MAX(salary) AS SecondHighestSalary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

#2
SELECT employee_id, name
FROM employees
GROUP BY employee_id, name
HAVING COUNT(DISTINCT department_id) > 1;

#3
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;


#4
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

#5
UPDATE employees
SET salary = salary * 1.1
WHERE performance_rating = 'Excellent';
