'''
1. Create a tuple whih contains the first four positive integers a and tuple b which contains
the next four positive integers
'''
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
print(a)
print(b)
'''
2. Create a new tuple c which combine the numbers from both tuples in any order
'''
c = a[:] + b[:]
print(c)
'''
3. Create a tuple d which is a sorted copy of c, leaving c unchanged.
'''
d = tuple(sorted(c))
print(d)


'''
4. Print third element of d.
'''
print(d[3])

'''
5. Print last three elements of d without using its length.
'''
print(d[-3::1])

'''
6. Print the length of d
'''
print(len(d))
