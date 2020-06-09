# -*- coding: UTF-8 -*-

# > Python knows a number of compound data types, used to group together other values.
# > The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets.
# > Lists might contain items of different types, but usually the items all have the same type.
print('''\
# Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.\
''')
squares = [1, 4, 9, 16, 25]
print(squares) # = [1, 4, 9, 16, 25]

# > Like strings (and all other built-in sequence type), lists can be indexed and sliced:
print('# Like strings (and all other built-in sequence type), lists can be indexed and sliced:')
print(squares[0]) # = 1 # indexing returns the item
print(squares[-1]) # = 25
print(squares[-3:]) # [9, 16, 25] # slicing returns a new list

# > All slice operations return a new list containing the requested elements.
# > This means that the following slice returns a new (shallow) copy of the list:
print(squares[:]) # = [1, 4, 9, 16, 25]

# > Lists also support operations like concatenation:
print('# Lists also support operations like concatenation:')
print(squares + [36, 49, 64, 81, 100]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# > Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
print('# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:')
cubes = [1, 8, 27, 65, 125] # something's wrong here
print(cubes) # = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3
print(cubes) # = [1, 8, 27, 64, 125]

# You can also add new items at the end of the list, by using the append() method
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(cubes) # = [1, 8, 27, 64, 125, 216, 343]

# > Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
print('# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters) # = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters) # = ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = [] # remove them
print(letters) # =  ['a', 'b', 'f', 'g']
letters[:] = [] # clear the list by replacing all the elements with an empty list
print(letters) # = []

# > The built-in function len() also applies to lists:
print('# The built-in function len() also applies to lists:')
letters = ['a', 'b', 'c', 'd']
print(len(letters)) # = 4

# > It is possible to nest lists (create lists containing other lists)
print('# It is possible to nest lists (create lists containing other lists)')
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x) # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) # ['a', 'b', 'c']
print(x[0][1]) # 'b'