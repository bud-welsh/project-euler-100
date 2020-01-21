# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

largest_prime = 0
prime = 2
start = 600851475143

if prime < start / 2:
  while largest_prime != start:
    if start % prime == 0:
      if prime > largest_prime:
        largest_prime = prime
        print(prime)
        start = start / prime
        prime = 2
      else:
        print(prime)
        start = start / prime
        prime = 2
    else:
      if prime == 2:
        prime = 3
      else:
        prime += 2
else:
  largest_prime = start
  print(largest_prime)


      
    