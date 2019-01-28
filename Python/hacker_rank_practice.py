x = int(input())
y = int(input())
z = int(input())
n = int(input())

# print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])
result = []
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if (a+b+c) != n:
                temp_list = []
                temp_list.append(a)
                temp_list.append(b)
                temp_list.append(c)
                result.append(temp_list)

print(result)