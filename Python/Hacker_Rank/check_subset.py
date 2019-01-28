t = int(input())

for i in range(0,t):
    n1 = int(input())
    a = set(list(map(int, input().split())))
    n2 = int(input())
    b = set(list(map(int, input().split())))
    print(a.issubset(b))