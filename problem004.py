# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

answer = 0
max_palindrome = 0


for first_number in range(999, 100, -1):
    for second_number in range(first_number, 100, -1):
        string_answer = str(first_number * second_number)
        if string_answer == string_answer[::-1]:
            answer = first_number * second_number
            if answer > max_palindrome:
                max_palindrome = answer

print(max_palindrome)
