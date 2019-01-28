'''
1. Create a list whih contains the first three odd positive integers a and list b which contains
the first three even positive integers
'''
a = [1, 3, 5]
b = [2, 4, 6]
print(a)
print(b)
'''
2. Create a new list c which combine the numbers from both lists (order is unimportant)
'''
c = a[:] + b[:]
print(c)
'''
3. Create a list d which is a sorted copy of c, leaving c unchanged.
'''
d = sorted(c)
print(d)
'''
4. Reverse d in-place.
'''
d.reverse()
print(d)
'''
5. Set forth element of c to 42
'''
c.insert(4,42)
print(c)
'''
6. Append 10 to the end of d.
'''
d.append(10)
print(d)
'''
7. Append 7, 8, 9 to the end of c
'''
c.append(7)
c.append(8)
c.append(9)
print(c)
'''
8. Print first three elements of c
'''
print(c[:3])
'''
9. Print the last element of d without using its length
'''
print(d[-1])
'''
10. Print the length of d
'''
print(len(d))
