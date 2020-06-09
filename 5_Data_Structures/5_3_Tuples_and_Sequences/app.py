# -*- coding: UTF-8 -*-

# > We saw that lists and strings have many common properties, such as indexing and slicing operations.
# > They are two examples of sequence data types (see Sequence Types — list, tuple, range).
# > Since Python is an evolving language, other sequence data types may be added.
# > There is also another standard sequence data type: the tuple.

# > A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
print(t[0]) # 12345
print(t) # (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
#t[0] = 888888
#Traceback (most recent call last):
#  File "app.py", line 16, in <module>
#    t[0] = 888888
#TypeError: 'tuple' object does not support item assignment
# but the can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v) # ([1, 2, 3], [3, 2, 1])

# > As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression).
# > It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.
#t[0] = 888888
#Traceback (most recent call last):
#  File "app.py", line 29, in <module>
#    t[0] = 888888
#TypeError: 'tuple' object does not support item assignment
s = 123, 456, []
print(s) # (123, 456, [])
s[2].append(1)
print(s) # (123, 456, [1])

# > Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
# > Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples).
r = 123, "456", 789
#r[1] = 456
#Traceback (most recent call last):
#  File "app.py", line 42, in <module>
#    r[1] = 456
#TypeError: 'tuple' object does not support item assignment
print(r[0], r[1], r[2]) # 123 456 789

# > Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
q = [123, 456, 789]
q[0] = 1230
for l in q:
    print(l)

# > A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these.
# > Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses).
# > Ugly, but effective. For example:
empty = ()
singleton = 'hello', # <-- note: trailing comma
print(len(empty)) # 0
print(len(singleton)) # 1
print(singleton) # ('hello',)

# > The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple.
# > The reverse operation is also possible:
print(t) # (12345, 54321, 'hello!')
x, y, z = t
print(x, y, z) # 12345 54321 hello!

# > This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side.
# > Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence.
# > Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
x, y, z = 12345, 54321, 'hello!'
x, y, z = t