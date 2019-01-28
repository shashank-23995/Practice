import itertools
# for animal in itertools.cycle(['cat','dog'],):
#     print(animal)

numbers = [1,2,3,4]
animals = ['cat', 'dog', 'fish']
for i in itertools.chain(numbers, animals):
    print(i)

# for i in itertools.repeat(1,3):
#     print(i)