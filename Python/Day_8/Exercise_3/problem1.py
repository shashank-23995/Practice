'''
1. Create dict dictionary which stores telephone numbers (as a string values), and populate it
with these key-value pair

Jane Doe    +27 555 5367
John Smith  +27 555 6254
Bob Stone   +27 555 5689
'''
dict = {
    "Jane Doe":"+27 555 5367",
    "John Smith":"+27 555 6254",
    "Bob Stone":"+27 555 5689"
}
print(dict)

'''
2. Change Jane's number to +27 555 1024
'''
dict["Jane Doe"] = "+27 555 1024"
print(dict)

'''
3. Add a new entry for a person called Anna Cooper with the phone number +27 555 3237
'''
dict["Anna Cooper"] = "+27 555 3237"

'''
4. Print Bob's number
'''
print(dict["Bob Stone"])

'''
5. Print the Bob's number in such a way that None would be printed if Bob's name were not 
in the dictionary
'''
print(dict.get("Bob Stone",None))

'''
6. Print all the keys. The format is unimportant, as long as they are all visible
'''
print(dict.keys())
'''
7. Print all the values
'''
print(dict.values())