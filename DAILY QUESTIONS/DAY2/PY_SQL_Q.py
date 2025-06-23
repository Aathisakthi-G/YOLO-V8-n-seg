# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:36:35 2025

@author: aathi
"""

#1
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True

#2
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed.")

#3
def sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

# Example usage
print(sum_of_evens([1, 2, 3, 4, 5]))  # Output: 6

#4
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example usage
print(find_longest_word("Find the longest word in this sentence"))  # Output: "sentence"

#5
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


#SQL

#1
SELECT department_id, COUNT(*) AS employee_count FROM employees GROUP BY department_id;

#2
SELECT * FROM employees WHERE salary > 50000;

#3
SELECT department_id, MAX(salary) AS highest_salary FROM employees GROUP BY department_id;

#4
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;

#5
UPDATE employees SET salary = salary * 1.1 WHERE employee_id = 101;
