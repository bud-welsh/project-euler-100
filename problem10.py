# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


# Variables
stopping_number = 2000000 # This is where to stop
sum_of_primes = 2 # Start at 2 because it makes the code easier to write
number = 3 # 3 is the first odd prime number
denominator = 3

# The Code
while number < stopping_number:
    if number / denominator != 1:
        if number % denominator != 0:
            denominator += 2
        else:
            number += 2
            denominator = 3
    else:
        sum_of_primes = sum_of_primes + number
        number += 2
        denominator = 3

print(sum_of_primes)
