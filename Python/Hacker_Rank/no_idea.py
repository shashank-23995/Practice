happiness = 0

n, m = map(int,input().split())
arr = list(map(int,input().split()))
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)
