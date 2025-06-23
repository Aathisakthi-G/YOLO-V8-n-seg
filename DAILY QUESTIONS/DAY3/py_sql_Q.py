# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:03 2025

@author: aathi
"""
#1
def find_primes(start, end):
    primes = []  # Initialize an empty list to store prime numbers

    for num in range(start, end + 1):  # Iterate through numbers in the given range
        if num > 1:  # Only consider numbers greater than 1 (as 1 is not prime)
            for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
                if num % i == 0:  # If divisible by any number, it's not prime
                    break  # Exit the loop
            else:
                primes.append(num)  # If the loop completes without break, it's a prime

    return primes  # Return the list of prime numbers

#2
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_words("Hello World! This is Python."))


#3
def find_min_max(lst):
    return min(lst), max(lst)

numbers = [10, 2, 45, 67, 1, 99]
print(find_min_max(numbers))

#4
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares)  # Output: [4, 16, 36, 64, 100]

#5
my_dict = {'apple': 50, 'banana': 30, 'cherry': 40}

# Ascending Order
sorted_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_asc)

# Descending Order
sorted_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_desc)


#SQL

#1
SELECT name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

#2
SELECT * FROM employees 
ORDER BY join_date DESC 
LIMIT 5;

#3
SELECT category, SUM(sales_amount) AS total_sales 
FROM sales 
GROUP BY category;

#4
SELECT name, customer_id 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id 
    FROM orders 
    WHERE total_amount > 5000);

#5
DELETE FROM sales 
WHERE id NOT IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY timestamp DESC) AS row_num 
        FROM sales
    ) AS ranked_rows 
    WHERE row_num = 1);
