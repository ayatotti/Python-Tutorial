# -*- coding: UTF-8 -*-

# > The list data type has some more methods.
# > Here are all of the methods of list objects:
item_list = []
print(item_list) # []

#list.append(x)
# > Add an item to the end of the list. Equivalent to a[len(a):] = [x].
item_list.append(0)
print(item_list) # [0]

#list.extend(iterable)
# > Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
extra_list = [1, 2]
item_list.extend(extra_list)
print(item_list) # [0, 1, 2]

item_list.append(extra_list) # append list in list
print(item_list) # [0, 1, 2, [1, 2]]

#list.insert(i, x)
# > Insert an item at a given position.
# > The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
item_list.insert(2, 0)
print(item_list) # [0, 1, 0, 2, [1, 2]]

#list.remove(x)
# > Remove the first item from the list whose value is equal to x.
# > It raises a ValueError if there is no such item.
item_list.remove(0)
print(item_list) # [1, 0, 2, [1, 2]]

#list.pop([i])
# > Remove the item at the given position in the list, and return it.
# > If no index is specified, a.pop() removes and returns the last item in the list.
# > (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position.
# > You will see this notation frequently in the Python Library Reference.)
print(item_list.pop(), item_list) # [1, 2] [1, 0, 2]
print(item_list.pop(1), item_list) # 0 [1, 2]

#list.clear()
# > Remove all items from the list. Equivalent to del a[:].
item_list.clear()
print(item_list) # []

#list.index(x[, start[, end]])
# > Return zero-based index in the list of the first item whose value is equal to x.
# > Raises a ValueError if there is no such item.
# > The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list.
# > The returned index is computed relative to the beginning of the full sequence rather than the start argument.
item_list = [0, 1, 2, 0, 3, 4]
print(item_list.index(0)) # 0
print(item_list.index(0, 1, 5)) # 3

#list.count(x)
# > Return the number of times x appears in the list.
print(item_list.count(0)) # 2

#list.sort(key=None, reverse=False)
# > Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
item_list.sort()
print(item_list) # [0, 0, 1, 2, 3, 4]
item_list.sort(reverse=True)
print(item_list) # [4, 3, 2, 1, 0, 0]

#list.reverse()
# > Reverse the elements of the list in place.
item_list.reverse() # [0, 0, 1, 2, 3, 4]
print(item_list)

#list.copy()
# > Return a shallow copy of the list. Equivalent to a[:].
copy_list = item_list.copy()
print(item_list, copy_list) # [0, 0, 1, 2, 3, 4] [0, 0, 1, 2, 3, 4]
print('identity of copy_list is', hex(id(copy_list)))
print('identity of item_list is', hex(id(item_list)))

# > You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None.
# > This is a design principle for all mutable data structures in Python.
