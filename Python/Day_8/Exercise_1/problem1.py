'''
1. Create a set whih contains the first four positive integers a and set b which contains
the first four odd positive integers
'''
a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
print(a)
print(b)
'''
2. Create a new set c which combine the numbers which are in a or b (or both)
'''
c = a.union(b)
print(c)
'''
3. Create a set d which all the elements in a but not in b
'''
d = a.difference(b)
print(d)
'''
4. Create a set e which all the elements in b but not in a
'''
e = b.difference(a)
print(e)
'''
5. Create a set f which contains all the elements which are in a and b
'''
f = a.intersection(b)
print(f)
'''
6. Create a set f which contains all the elements which are in either a  or in b but not both
'''
b = a.symmetric_difference(b)
print(f)
'''
7. Print the number of elements in c
'''
print(len(c))
