# -*- coding: UTF-8 -*-

# The for statement in Python differs a bit from what you may be used to in C or Pascal.
# > Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
print('''\
# The for statement in Python differs a bit from what you may be used to in C or Pascal.
# Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.\
''')

# Measure some string:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print()

# > If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy.
# > Iterating over a sequence does not implicitly make a copy.
# > The slice notation makes this especially convenient:
print('''\
# If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy.
# Iterating over a sequence does not implicitly make a copy.
# The slice notation makes this especially convenient:\
''')
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words) # = ['defenestrate', 'cat', 'window', 'defenestrate']

# > With for w in words:, the example would attempt to create an infinite list, inserting defenestrate over and over again.
#words = ['cat', 'window', 'defenestrate']
#for w in words:
#    if len(w) > 6:
#        words.insert(0, w)
#    print(w)