'''
5. Rewrite the previous program so that it has two loops - one which collects and stores
the numbers and one which processesthem.
'''

print("Enter 10 floating-point numbers: ")
count = 0
float_list = []
sum = 0.0
product = 1.0
while count < 10:
    number = float(input("Enter number: "))
    float_list.append(number)
    count += 1
    
for i in float_list:
    sum += number
    product *= number

average = sum/len(float_list)
# print("sum = %f \n product = %f \n average = %f"% sum, product, average)
print("sum = %f"% sum)
print("product = %f"% product)
print("average = %f"% average)