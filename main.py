'''
CodeWars kata codewars.com

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
Examples:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
'''


def summation(num):
    my_sum = 0
    i=0
    while i <= num:
        my_sum = my_sum + i
        
        i+=1
    return my_sum
#--------someone else's solution
def summation(num):
    return (1+num) * num / 2
