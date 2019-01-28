# entr = [[int(x) for x in input().split()] for i in range(int(input()))]
# print(entr)

n1 = int(input())
a_list = input().split()
n2 = int(input())
b_list = input().split()
# for i in range(n1):
#     a_list.append(int(input())) 

# n2 = int(input())
# for i in range(n2):
#     b_list.append(int(input()))

a = set(a_list)
b = set(b_list)
result = list(a.symmetric_difference(b))
# for i in result:
#     print(i)

print(sorted(result))