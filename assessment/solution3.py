#!/usr/bin/python3

# You're given a number n=10
# There are four prime numbers less than n (2, 3, 5 and 7)
# The sum of these prime numbers is s=17
# If n=2,000,000 then find s
__author__ = 'Onyedikachi Udeh'
n = 2000000

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

print('Processing...')
the_sum = 0 
for each in range(2000000): 
    if isPrime(each):
            the_sum += each
print(f'The sum of all prime numbers less than {n} is ', the_sum)
###############################################################
# OUTPUT
###############################################################
# Processing...
# The sum of all prime numbers less than 2000000 is  142913828922