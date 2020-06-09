# -*- coding: UTF-8 -*-

# > Python also includes a data type for sets.
# > A set is an unordered collection with no duplicate elements.
# > Basic uses include membership testing and eliminating duplicate entries.
# > Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# > Curly braces or the set() function can be used to create sets.
# > Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

# > Here is a brief demonstration:
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'orange', 'apple', 'pear', 'banana'} # show that duplicates have been removed
print('orange' in basket) # True
print('crabgrass' in basket) # False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a) # {'c', 'a', 'd', 'b', 'r'} # unique letters in a
print(a - b) # {'d', 'b', 'r'} # letters in a but not in b
print(a | b) # {'c', 'm', 'a', 'l', 'd', 'b', 'r', 'z'} # letters in a or b or both
print(a & b) # {'c', 'a'} # letters in both a and b
print(a ^ b) # {'m', 'd', 'b', 'r', 'l', 'z'} # letters in a or b but not both

# > Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'r', 'd'}
