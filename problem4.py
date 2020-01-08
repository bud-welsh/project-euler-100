# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

first_number = 92
second_number = 99
answer = 1
reverse_answer = 0
remainder = 0
store = 0


while reverse_answer != answer:
  answer = first_number * second_number 
  store = answer

  while store > 0:
    reverse_answer = reverse_answer * 10
    remainder = store % 10
    store = ((store - remainder) / 10)
    reverse_answer = reverse_answer + remainder
    
  print(answer)
  print(reverse_answer)
  print(first_number)
  print(second_number)
  print(remainder)
  print(store)

  first_number = (first_number - 1)
  remainder = 0
  # answer = 1
  # reverse_answer = 0
  store = 0

  print(first_number)
  print(remainder)
  print(store)

#   if first_number > 0:
#     first_number = first_number - 1
#     if first_number == 1:
#       first_number = 99
#       second_number = second_number - 1
#       if second_number == 1:
#         first_number = 91
#         second_number = 99
#       else:
#         pass
#     else:
#       pass
#   else:
#     pass
