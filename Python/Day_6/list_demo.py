synerzip@ULTP-348:~/Desktop/Practice/Python$ python hello.py
Hello World
synerzip@ULTP-348:~/Desktop/Practice/Python$ ls
addition_algorithm.txt  hello.py
synerzip@ULTP-348:~/Desktop/Practice/Python$ sudo chmod +x hello.py
[sudo] password for synerzip: 
chmod: cannot access 'hello.py': No such file or directory
synerzip@ULTP-348:~/Desktop/Practice/Python$ cd Day_1
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1$ ls
Exercise_1  Python_practice
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1$ cd pyt
bash: cd: pyt: No such file or directory
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1$ cd Python_practice/
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ sudo chmod +x hello.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ ls
addition_algorithm.txt  hello.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ ./hello.py
Hello World
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1number=10;
  File "<stdin>", line 1
    1number=10;
          ^
SyntaxError: invalid syntax
>>> problem2.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'problem2' is not defined
>>> python problem2.py
  File "<stdin>", line 1
    python problem2.py
                  ^
SyntaxError: invalid syntax
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ ls
addition_algorithm.txt  hello.py  problem2.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> python problem2.py
  File "<stdin>", line 1
    python problem2.py
                  ^
SyntaxError: invalid syntax
>>> python problem_2.py
  File "<stdin>", line 1
    python problem_2.py
                   ^
SyntaxError: invalid syntax
>>> python Indention.py
  File "<stdin>", line 1
    python Indention.py
                   ^
SyntaxError: invalid syntax
>>> python Indention.py
  File "<stdin>", line 1
    python Indention.py
                   ^
SyntaxError: invalid syntax
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python Indention.py
Which day is today
It's Tuesday
Print this no matter what
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python Indention.py
Which day is today
Print this no matter what
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> type(12)
<class 'int'>
>>> type(-12)
<class 'int'>
>>> number_1 = 10
>>> type(number_1)
<class 'int'>
>>> type(1.4)
<class 'float'>
>>> 4 + 2 / 2
5.0
>>> 4 + 2 // 2
5
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ ls
addition_algorithm.txt  hello.py  Indention.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1/Python_practice$ cd ..
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_1$ cd ..
synerzip@ULTP-348:~/Desktop/Practice/Python$ cd Day_3
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ ls
string_formstting.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_formatting.py
python: can't open file 'string_formatting.py': [Errno 2] No such file or directory
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_formstting.py
Hello My name is Joe.
Hello My name is Joe and I am 29 years old.
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_formatting.py
Hello My name is Joe.
Hello My name is Joe and I am 29 years old.
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_formatting.py
Hello My name is Joe.
Traceback (most recent call last):
  File "string_formatting.py", line 4, in <module>
    print("Hello My name is %s and I am %d years old."%(age,name))
TypeError: %d format: a number is required, not str
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_formatting.py
Hello My name is Joe.
Hello My name is Joe and I am 29 years old.
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('This is one line. \nThis isanother line')
This is one line. 
This isanother line
>>> print('This is one line. \tThis is another line.')
This is one line. 	This is another line.
>>> print('"Hi! I\'m Joe," he said.')
"Hi! I'm Joe," he said.
>>> print("\"Hi! I'm Joe,\" he said.")
"Hi! I'm Joe," he said.
>>> print('"Hi! I'm Joe," he said.')
  File "<stdin>", line 1
    print('"Hi! I'm Joe," he said.')
                  ^
SyntaxError: invalid syntax
>>> print("\"Hi! I'm Joe," he said.")
  File "<stdin>", line 1
    print("\"Hi! I'm Joe," he said.")
                            ^
SyntaxError: invalid syntax
>>> print('"Hi! I'm Joe," he said.')
  File "<stdin>", line 1
    print('"Hi! I'm Joe," he said.')
                  ^
SyntaxError: invalid syntax
>>> print("\"Hi! I'm Joe," he said.")
  File "<stdin>", line 1
    print("\"Hi! I'm Joe," he said.")
                            ^
SyntaxError: invalid syntax
>>> print("\"Hi! I'm Joe,\" he said.")
"Hi! I'm Joe," he said.
>>> print("\\"Hi! I'm Joe,\" he said.")
  File "<stdin>", line 1
    print("\\"Hi! I'm Joe,\" he said.")
               ^
SyntaxError: invalid syntax
>>> print("\"Hi! I'm Joe,\\" he said.")
  File "<stdin>", line 1
    print("\"Hi! I'm Joe,\\" he said.")
                              ^
SyntaxError: invalid syntax
>>> print("\"Hi! I'm Joe,\" he said.")
"Hi! I'm Joe," he said.
>>> print(r"Hello!"\n)
  File "<stdin>", line 1
    print(r"Hello!"\n)
                     ^
SyntaxError: unexpected character after line continuation character
>>> print(r"Hello!\n")
Hello!\n
>>> string_one = '''Hello,"said Jane
... "Hi," said Bob.'''
>>> print(string_one)
Hello,"said Jane
"Hi," said Bob.
>>> string_one
'Hello,"said Jane\n"Hi," said Bob.'
>>> type(lower)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lower' is not defined
>>> type(lower())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lower' is not defined
>>> type(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> name = "Jane Smith"
>>> type(name)
<class 'str'>
>>> type(name.lower)
<class 'builtin_function_or_method'>
>>> type(name.lower())
<class 'str'>
>>> type(name.lower)
<class 'builtin_function_or_method'>
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python string_operations.py
10
jane smith
Jane Smith
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 20 % 7 // 3
2
>>> 2 ** 3 ** 2
512
>>> 3**2
9
>>> 1 // 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> type(1.0)
<class 'float'>
>>> 7.5e-3
0.0075
>>> 1.12e4
11200.0
>>> type(1.12e4)
<class 'float'>
>>> 1.5 + 2
3.5
>>> 1.5 // 2.0
0.0
>>> 1.5 / 2.0
0.75
>>> 1.5 ** 2
2.25
>>> 1.5**2
2.25
>>> 1.5*2
3.0
>>> 1.5**2
2.25
>>> 1 / 2 
0.5
>>> -3 // 2
-2
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 1e1000
inf
>>> -1e1000
-inf
>>> type(1e1000)
<class 'float'>
>>> count, result, total = 1, 2, 3
>>> print(count)
1
>>> print(result)
2
>>> print(total)
3
>>> 
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_3$ cd ..
synerzip@ULTP-348:~/Desktop/Practice/Python$ ls
Day_1  Day_2  Day_3  Day_4  python_practice
synerzip@ULTP-348:~/Desktop/Practice/Python$ cd Day_4
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_4$ ls
variables.py
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_4$ python variables.py 
  File "variables.py", line 4
    if a==0
          ^
SyntaxError: invalid syntax
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_4$ python variables.py 
7
3
0
1
Traceback (most recent call last):
  File "variables.py", line 22, in <module>
    print(c)
NameError: name 'c' is not defined
synerzip@ULTP-348:~/Desktop/Practice/Python/Day_4$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 3
>>> 3 = 4
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> 3 = a
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> b = 0
>>> a + b = 3
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> a = b = 0
>>> a = 0 = b
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> count = 0
>>> count = count + 1
>>> print(count)
1
>>> count = count + 1
>>> print(count)
2
>>> count = count + 1
>>> print(count)
3
>>> count += 1
>>> print(count)
4
>>> count += 1
>>> print(count)
5
>>> type(input)
<class 'builtin_function_or_method'>
>>> print(5)
5
>>> print(6.7)
6.7
>>> print("3" + 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> print("3%d"% 4)
34
>>> print(int(3) + 4)
7
>>> print(int("3") + 4)
7
>>> print(int("abc"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
>>> print(int("3.7"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.7'
>>> print(int(float("3.7")))
3
>>> bool(-34)
True
>>> bool(-0.0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool("abc")
True
>>> bool("abc")
True
>>> bool(@)
  File "<stdin>", line 1
    bool(@)
         ^
SyntaxError: invalid syntax
>>> bool([])
False
>>> bool([1,w,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'w' is not defined
>>> bool([1,2,3])
True
>>> bool([0,0,0])
True
>>> bool("0")
True
>>> bool("False")
True
>>> bool(False)
False
>>> bool(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> bool(True)
True
>>> age = 17
>>> if age < 18:
... print("cannot vote")
  File "<stdin>", line 2
    print("cannot vote")
        ^
IndentationError: expected an indented block
>>> age = 17
>>> if age < 18:
...     print("cannot vote")
... 
cannot vote
>>> a = 2
>>> b = 2
>>> a == b
True
>>> a is b
True
>>> a = 10
>>> b = 5
>>> a is not b
True
>>> a != b
True
>>> a is not b
True
>>> x = 0
>>> x +=1
>>> x = 0
>>> score = 60
>>> result = "Pass" if (score >= 50) else "Fail"
>>> print(result)
Pass
>>> name = "Jane"
>>> x = 0
>>> type(none)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'none' is not defined
>>> type(None)
<class 'NoneType'>
>>> list
<class 'list'>
>>> 


synerzip@ULTP-348:~/Desktop/Practice/Python$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> list
<class 'list'>
>>> animals = ['cat', 'dog', 'fish', 'bison']
>>> type(animals)
<class 'list'>
>>> numbers = [1,7,34,20]
>>> my_list = []
>>> a = 10
>>> b = 20
>>> c = 30
>>> things = [a,b,c]
>>> print(things)
[10, 20, 30]
>>> print(animals[0])
cat
>>> print(numbers[1])
7
>>> print(animals[6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(animals[-1])
bison
>>> print(animals[-2])
fish
>>> animals
['cat', 'dog', 'fish', 'bison']
>>> animals[1:3]
['dog', 'fish']
>>> animals[1:-1]
['dog', 'fish']
>>> animals[0:-1]
['cat', 'dog', 'fish']
>>> animals[1:-1]
['dog', 'fish']
>>> animals[1:0]
[]
>>> animals[1:-1]
['dog', 'fish']
>>> animals[:]
['cat', 'dog', 'fish', 'bison']
>>> animals[1:]
['dog', 'fish', 'bison']
>>> animals[-1:-3]
[]
>>> animals[-3:1]
[]
>>> animals[-3:-1]
['dog', 'fish']
>>> animals[-4:-1]
['cat', 'dog', 'fish']
>>> animals[-1:-3]
[]
>>> animals[:]
['cat', 'dog', 'fish', 'bison']
>>> animals[]
  File "<stdin>", line 1
    animals[]
            ^
SyntaxError: invalid syntax
>>> animals[:]
['cat', 'dog', 'fish', 'bison']
>>> numbers[::2]
[1, 34]
>>> numbers
[1, 7, 34, 20]
>>> numbers[::2]
[1, 34]
>>> animals
['cat', 'dog', 'fish', 'bison']
>>> animals[::2]
['cat', 'fish']
>>> animals[3] = "hamster"
>>> animals
['cat', 'dog', 'fish', 'hamster']
>>> type(animals)
<class 'list'>
>>> dir(animals)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> animals.append("squirrel")
>>> animals
['cat', 'dog', 'fish', 'hamster', 'squirrel']
>>> del animals[2]
>>> animals
['cat', 'dog', 'hamster', 'squirrel']
>>> pets = animals
>>> animals.append('fish')
>>> pets
['cat', 'dog', 'hamster', 'squirrel', 'fish']
>>> pets = animals[:]
>>> animals.append('canary')
>>> animals
['cat', 'dog', 'hamster', 'squirrel', 'fish', 'canary']
>>> pets
['cat', 'dog', 'hamster', 'squirrel', 'fish']
>>> numbers
[1, 7, 34, 20]
>>> my_number = 67
>>> if my_number in numbers:
...     print("%d is in the list"% my_number)
...
>>> my_number = 34
>>> if my_number in numbers:
...     print("%d is in the list"% my_number)
...
34 is in the list
>>> my_number = 67
>>> if my_number not in numbers:
...     print("%d is not in the list"% my_number)
...
67 is not in the list
>>> len(animals)
6
>>> sum
<built-in function sum>
>>> sum(numbers)
62
>>> any
<built-in function any>
>>> numbers
[1, 7, 34, 20]
>>> numbers.append(20)
>>> numbers.count(20)
2
>>> another_numbers = [56,2,12]
>>> another_numbers
[56, 2, 12]
>>> numbers.append(another_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'another_number' is not defined
>>> numbers.append(another_numbers)
>>> numbers
[1, 7, 34, 20, 20, [56, 2, 12]]
>>> numbers[-1]
[56, 2, 12]
>>> del numbers[-1]
>>> numbers
[1, 7, 34, 20, 20]
>>> numbers.extend(another_numbers)
>>> numbers
[1, 7, 34, 20, 20, 56, 2, 12]
>>> numbers.index(12)
7
>>> numbers.index(34)
2
>>> numbers.index(20)
3
>>> numbers.index(55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 55 is not in list
>>> numbers.insert(0, 45)
>>> numbers
[45, 1, 7, 34, 20, 20, 56, 2, 12]
>>> numbers.remove(12)
>>> numbers
[45, 1, 7, 34, 20, 20, 56, 2]
>>> my_number = numbers.pop()
>>> my_number
2
>>> sorted
<built-in function sorted>
>>> sorted(numbers)
[1, 7, 20, 20, 34, 45, 56]
>>> numbers
[45, 1, 7, 34, 20, 20, 56]
>>> reversed
<class 'reversed'>
>>> reversed(numbers)
<list_reverseiterator object at 0x7f844ce70a58>
>>> list(reversed(numbers))
[56, 20, 20, 34, 7, 1, 45]
>>> numbers
[45, 1, 7, 34, 20, 20, 56]
>>> numbers.sort()
>>> numbers
[1, 7, 20, 20, 34, 45, 56]
>>> numbers.reverse()
>>> numbers
[56, 45, 34, 20, 20, 7, 1]
>>> sorted(numbers, reverse=True)
[56, 45, 34, 20, 20, 7, 1]
>>> sorted(numbers, reverse=False)
[1, 7, 20, 20, 34, 45, 56]
>>> sorted(numbers, reverse=True)
[56, 45, 34, 20, 20, 7, 1]
>>> list1 = [1,2,3]
>>> list2 = [4,5,6]
>>> list1 + list2
[1, 2, 3, 4, 5, 6]
>>> [1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> [1,2,3] - [2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> dir(animals)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> numbers.clear()
>>> numbers
[]
>>>
KeyboardInterrupt
>>>
