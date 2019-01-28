'''
1. Convert a list which contains the number 1, 1, 2, 3 and 3 and convert it to a tuple
'''
a = tuple([1,1,2,3,3])
print(a)
'''
2. Convert a to a list b. Print its length
'''
b = list(a)

'''
3. Convert b to a set c. Print its length
'''
c = set(b)

'''
4. Convert c to a list d. Print its length
'''
d = list(c)

'''
5. Create a range which starts at 1 and ends at 10. Convert it to a list e.
'''
print(list(range(1,11)))

'''
6. Create a dictionary dict from the previous example. Create a list t which contains all the
key-value pairs from the dictionary as tuples
'''
dict = {
    'Bob Stone': '+27 555 5689', 
    'John Smith': '+27 555 6254', 
    'Jane Doe': '+27 555 5367', 
    'Anna Cooper': '+27 555 3237'
    }
t = dict.items()
print(t)

'''
7. Create a list v of all the values in the dictionsry
'''
v = dict.keys()
print(v)
'''
8. Create a list k from all keys in the dictionary
'''
k = dict.values()
print(k)

'''
9. Create a string s which contains the word "antidiestablishmentarianism".
Use the sorted function on it. What is the output type ? Concatenate the letters in the
output
'''
s = "antidiestablishmentarianism"
s2 = sorted(s)
print(s2)
"Output type - list"
'''
10. Split the string "the quick brown fox jumped over the lazy dog" into a list w of 
indvidual words.
'''
w = "the quick brown fox jumped over the lazy dog".split()
print(w)