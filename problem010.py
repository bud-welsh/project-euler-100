# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

n = 2000000
p = 2
prime = [True for i in range(n + 1)]

while (p * p <= n): 
    if (prime[p] == True): 
        for i in range(p * 2, n + 1, p): 
            prime[i] = False
    p += 1
prime[0]= False
prime[1]= False

sum_of_primes = 0 
for p in range(n + 1): 
    if prime[p]:
        sum_of_primes = sum_of_primes + p

print(sum_of_primes) 
