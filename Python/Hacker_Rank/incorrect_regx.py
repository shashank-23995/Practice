import re

t = int(input())
for i in range(t):
    expression = input()
    try:
        re.compile(expression)
        is_valid = True
        print(is_valid)
    except re.error:
        is_valid = False
        print(is_valid)