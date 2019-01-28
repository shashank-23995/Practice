'''
3. Write a program which finds the factorial of a given number.
E.g. 3 factorial or 3! equal to 3 * 2 * 1; 5! is equal to 5 * 4 * 3 * 2 * 1 etc...
Your program should only contain a single loop.
'''

number = int(input("Enter number: "))
factorial = 1
for i in range(1,number + 1):
    factorial = factorial * i

print("Factorial = %d"% factorial)