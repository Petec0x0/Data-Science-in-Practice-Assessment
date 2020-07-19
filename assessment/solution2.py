#!/usr/bin/python3

# What is the 10001st prime number?
__author__ = 'Onyedikachi Udeh'

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
count = 0 
for each in range(1000000): 
    if isPrime(each):
            count += 1
            if count == 10001:
                print('The 10001st prime is',each)
                break

###############################################################
# OUTPUT
###############################################################
# Processing...
# The 10001st prime is 104743