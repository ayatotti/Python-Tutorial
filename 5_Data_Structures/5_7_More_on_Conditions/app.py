# -*- coding: UTF-8 -*-

# > The conditions used in while and if statements can contain any operators, not just comparisons.

# > The comparison operators in and not in check whether a value occurs (does not occur) in a sequence.
# > The operators is and is not compare whether two objects are really the same object; this only matters for mutable objects like lists.
# > All comparison operators have the same priority, which is lower than that of all numerical operators.

# > Comparisons can be chained.
# > For example, a < b == c tests whether a is less than b and moreover b equals c.
print(1 < 1 + 1 == 2) # True # 1 < (1 + 1) and (1 + 1) == 2
print(1 < 1 + 1 and 1 + 1 == 2) # True and True : True
print(1 < 1 == 1) # False and True : False
print()

# > Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not.
# > These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C.
# > As always, parentheses can be used to express the desired composition.
print(True and not False or False) # True
print((True and (not False)) or False) # True
print()

# > The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
# > For example, if A and C are true but B is false, A and B and C does not evaluate the expression C.
# > When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.
print(True and False and None) # False
print(True or None) # True
print(True and None) # None

l = []
print(True and False and l.append(1)) # False
print(l) # [] # not append 1
print(True or l.append(1)) # True
print(l) # [] # not append 1
print(True and l.append(1)) # None
print(l) # [1] # append 1
print()

# > It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null) # Trondheim

# > Note that in Python, unlike C, assignment cannot occur inside expressions.
# > C programmers may grumble about this, but it avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.
