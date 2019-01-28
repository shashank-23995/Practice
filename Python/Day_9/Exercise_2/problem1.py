'''
1. Create a list a which contains htree tuples. The first tuple should contain single 
element, the second two elements and third three elements
'''
a = [(1), (1,2), (1,2,3)]
print(a)
'''
2. Print the second element of the second element of a
'''
print(a[1][1])

'''
3. Create a list b which contains four lists, each of which contains four elements.
'''
b = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(b)

'''
4. Print the last two elements of the first element of b
'''
print(b[0][-2::1])