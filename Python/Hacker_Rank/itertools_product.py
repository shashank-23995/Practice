import itertools

a = list(map(int,input().split()))
b = list(map(int,input().split()))

result = list(itertools.product(a, b))
for i in result:
    print(i, end=" ")
# print(list(result))