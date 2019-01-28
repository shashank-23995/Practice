n = int(input())
a = set(list(map(int, input().split())))
instructions = int(input())

for i in range(instructions):
    row = input()
    row_list = list(row)
    p1 = row_list[0]
    p2 = int(row_list[1])
    