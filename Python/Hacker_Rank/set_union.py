n1 = int(input())
arr1 = set(list(map(int, input().split())))
n2 = int(input())
arr2 = set(list(map(int, input().split())))
print(len(arr1.union(arr2)))