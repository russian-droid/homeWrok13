'''
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
Examples:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
'''


my_sum = 0
i=0
n=8
#replace this pass (a do-nothing) statement with your code
while i <= n:
    my_sum = my_sum + i
    i+=1
print(my_sum)
