# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

#2
# Example using the `|` operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Example using `update` method
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

#3
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)  # Output: [3, 4]

#4
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci_gen(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34

#5
import copy

list1 = [[1, 2], [3, 4]]
shallow = copy.copy(list1)
shallow[0][0] = 99
print(list1)  # Output: [[99, 2], [3, 4]]

deep = copy.deepcopy(list1)
deep[0][0] = 100
print(list1)  # Output: [[99, 2], [3, 4]]

#SQL

#1
SELECT salary FROM employees ORDER BY salary DESC LIMIT 3;

#2
SELECT column1, column2, COUNT(*) FROM table_name GROUP BY column1, column2 HAVING COUNT(*) > 1;

#3
SELECT department_id, AVG(salary) AS avg_salary FROM employees GROUP BY department_id;

#4
SELECT e.employee_id, e.name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.department_id;

#5
DELETE FROM table_name WHERE column_name IS NULL;
