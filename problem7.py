# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

# Get the nth number to define which prime number we are looking to find
prime_number_to_find = 10001
counter = 3 # 3 is the 2nd prime number and that seems like a good place to start
number = 5
denominator = 3
found_prime_number = 0 

while counter != prime_number_to_find + 1:
    if number / denominator != 1:
        if number % denominator != 0:
            denominator += 1
        else:
            number += 2
            denominator = 3
    else:
        found_prime_number = number
        counter += 1
        denominator = 3
        number += 2


print(found_prime_number)
