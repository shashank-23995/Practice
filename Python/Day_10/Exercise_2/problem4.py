'''
4. Write a program which prompts the user for 10 floating-point numbers and calculates
their sum, product and average. Your program should only contain a single loop.
'''

print("Enter 10 floating-point numbers: ")
count = 0
float_list = []
sum = 0.0
product = 1.0
while count < 10:
    number = float(input("Enter number: "))
    float_list.append(number)
    sum += number
    product *= number
    count += 1

average = sum/len(float_list)
# print("sum = %f \n product = %f \n average = %f"% sum, product, average)
print("sum = %f"% sum)
print("product = %f"% product)
print("average = %f"% average)
