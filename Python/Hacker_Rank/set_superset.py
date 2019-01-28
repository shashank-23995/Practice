a = set(list(map(int, input().split())))
result = []
n = int(input())
for i in range(n):
    b = set(list(map(int, input().split())))
    result.append(a.issuperset(b))
    
print(all(result))