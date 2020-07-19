#!/usr/bin/python3

# Given the list of numbers 1 through 10
# Sum_of_Squares is 385
# Square_of_Sum is 3025
# (Square_of_Sum -Sum_of_Squares) is 2640
# Carry out this same exercise for the list of numbers 1 through 500
__author__ = 'Onyedikachi Udeh'

start_from = 1 # start point
stop_at = 500 # end point

# calculate the sum of squares
sum_of_squares = 0
for i in range(start_from,stop_at+1):
    cal = i * i
    sum_of_squares += cal

# calculate the square of sum
add = 0
for j in range(start_from,stop_at+1):
    add += j

square_of_sum = add * add
print("Sum of Squares is ",sum_of_squares) # print the value of sum_of_squares
print("Squares of Sum is ",square_of_sum)  # print the value of square_of_sum
print("(Square_of_Sum - Sum_of_Squares) is", square_of_sum - sum_of_squares) # print the value of (Square_of_Sum - Sum_of_Squares)


###############################################################
# OUTPUT
###############################################################
# Sum of Squares is  41791750
# Squares of Sum is  15687562500
# (Square_of_Sum - Sum_of_Squares) is 15645770750