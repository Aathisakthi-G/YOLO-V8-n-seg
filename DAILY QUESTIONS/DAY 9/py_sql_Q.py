# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print(sum_of_digits(1234))  # Output: 10


#2
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]

#3
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2024))  # Output: True
print(is_leap_year(2023))  # Output: False

#4
a = [1, 2, 3]
b = a  
c = [1, 2, 3]

print(a == c)  # True (same values)
print(a is c)  # False (different objects in memory)
print(a is b)  # True (same memory reference)

#5
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"


#SQL

#1
SELECT e.employee_id, e.name
FROM employees e
LEFT JOIN sales s ON e.employee_id = s.employee_id 
    AND s.sale_date >= DATEADD(MONTH, -1, GETDATE())
WHERE s.employee_id IS NULL;

#2
SELECT name, age, 
CASE 
    WHEN age < 18 THEN 'Minor' 
    WHEN age BETWEEN 18 AND 60 THEN 'Adult' 
    ELSE 'Senior'
END AS AgeCategory
FROM customers;

#3
SELECT product_id, 
       SUM(sales_amount) AS total_sales, 
       (SUM(sales_amount) * 100.0) / (SELECT SUM(sales_amount) FROM sales) AS percentage_contribution
FROM sales
GROUP BY product_id;


#4
SELECT column1, column2, COUNT(*)
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1;

DELETE FROM table_name 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM table_name 
    GROUP BY column1, column2
);

#5
SELECT e.name 
FROM employees e
WHERE e.manager_id = (SELECT manager_id FROM employees WHERE name = 'John Doe');

