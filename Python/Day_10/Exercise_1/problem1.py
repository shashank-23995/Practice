# Write a program which uses while loop to sum the squares of the integers 
# (starting from 1) until the toal until the total exceeds 200. Print the final total and 
# the last number to be squared and added

number = 1
total = 0
while(total <= 200):
    total = total + (number * number)
    number += 1

print("total = %d"% total)
print("last number to be squared = %d"% number - 1)