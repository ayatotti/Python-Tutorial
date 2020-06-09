# -*- coding: UTF-8 -*-

# > There is a way to remove an item from a list given its index instead of its value: the del statement.
# > This differs from the pop() method which returns a value.
# > The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice).
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a) # [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a) # [1, 66.25, 1234.5]
del a[:]
print(a) # []

# > del can also be used to delete entire variables:
del a
#print(a)
#Traceback (most recent call last):
#  File "app.py", line 16, in <module>
#    print(a)
#NameError: name 'a' is not defined

# > Referencing the name a hereafter is an error (at least until another value is assigned to # it).
# > We’ll find other uses for del later.