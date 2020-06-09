# -*- coding: UTF-8 -*-

# > If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
print('If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:')
for i in range(5):
        print(i)

print()

# > The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10.
# > It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’)
print('''\
# The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10.
#  It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’)\
''')
for i in range(5, 10): # From 5 to 10
        print(i, end=',')
print()

for i in range(0, 10, 3): # From 0 to 10 in 3 steps
        print(i, end=',')
print()

for i in range(-10, -100, -30): # From -10 to -100 in -30 steps
        print(i, end=',')
print()

print()

# > To iterate over the indices of a sequence, you can combine range() and len() as follows:
print('To iterate over the indices of a sequence, you can combine range() and len() as follows:')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
        print(i, a[i])

# > In most such cases, however, it is convenient to use the enumerate() function.

print()

# > A strange thing happens if you just print a range:
print('# A strange thing happens if you just print a range:')
print(range(10)) # = range(0, 10)

# > In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
# > It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# > We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
# > We have seen that the for statement is such an iterator.
# > The function list() is another; it creates lists from iterables:
print('''\
# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
# It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
# We have seen that the for statement is such an iterator.
# The function list() is another; it creates lists from iterables:\
''')
print(list(range(5))) # = [0, 1, 2, 3, 4]