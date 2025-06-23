# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Output: 120

#2
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("Hello"))  # Output: "olleH"

#3
def intersection(list1, list2):
    return list(set(list1) & set(list2))
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

#4
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

#5
def count_vowels_consonants(s):
    vowels = "aeiou"
    vowels_count = sum(1 for char in s.lower() if char in vowels)
    consonants_count = sum(1 for char in s.lower() if char.isalpha() and char not in vowels)
    return vowels_count, consonants_count
print(count_vowels_consonants("Hello World"))  # Output: (3, 7)

#SQL

#1
SELECT name 
FROM employees 
WHERE joining_date >= CURDATE() - INTERVAL 6 MONTH;

#2
SELECT category, SUM(revenue) AS total_revenue 
FROM sales 
GROUP BY category;


#3
SELECT customer_id 
FROM orders 
GROUP BY customer_id 
HAVING COUNT(order_id) = 3;


#4
-- INNER JOIN
SELECT orders.order_id, customers.name 
FROM orders 
INNER JOIN customers ON orders.customer_id = customers.id;

-- LEFT JOIN
SELECT orders.order_id, customers.name 
FROM orders 
LEFT JOIN customers ON orders.customer_id = customers.id;


#5
SELECT product_id, order_date, revenue,
       SUM(revenue) OVER (PARTITION BY product_id ORDER BY order_date) AS running_total
FROM sales;
