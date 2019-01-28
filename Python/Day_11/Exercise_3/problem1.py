'''
Write a program which repeatedly prompts the user for an integer.
If the integer is even prints the integer.
If the number is odd don't print anything.
Exit the program if user enters 99
'''
while True:
    number = int(input("Enter integer: "))
    if number == 99:
        break
    else:
        if number % 2 == 0:
            print(number)
        