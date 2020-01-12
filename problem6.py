# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Find sum of the squares

# Variables
sum_squares = 0
number_sum_squares = 1

while number_sum_squares <= 100:
    squares = number_sum_squares ** 2
    sum_squares = sum_squares + squares
    number_sum_squares += 1

# Find square of the sum

# Variables
total_sum = 0
number_to_add = 1

while number_to_add <= 100:
    total_sum = total_sum + number_to_add
    number_to_add += 1
square_sum = total_sum ** 2


# Difference between sum_squares and square_sum which is the answer to the question
answer = square_sum - sum_squares
print(str(square_sum) + " - " + str(sum_squares) + " = " + str(answer))