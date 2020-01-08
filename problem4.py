# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

first_number = 99
second_number = 99
number = first_number * second_number
string_number = str(number)
list_number = list(string_number)
reverse_list = list(reversed(list_number))
print(str(first_number) + '*' + str(second_number) + '=' + str(number))

while list_number != reverse_list:
  if list_number == reverse_list:
    print(str(first_number) + '*' + str(second_number) + '=' + str(number))
  else:
    if first_number >= 10:
      first_number = first_number - 1
      print(str(first_number) + '*' + str(second_number) + '=' + str(number))
    else:
      first_number = 99
      second_number = second_number - 1
      print(str(first_number) + '*' + str(second_number) + '=' + str(number))
