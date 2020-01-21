total = 0
fib_start = 0
fib_next = 1
fib_sum = 1

while fib_sum <= 4000000:
  if fib_sum % 2 == 0:
    total += fib_sum
    fib_start = fib_next
    fib_next = fib_sum
    fib_sum = fib_start + fib_next
  else:
    fib_start = fib_next
    fib_next = fib_sum
    fib_sum = fib_start + fib_next

print(total)