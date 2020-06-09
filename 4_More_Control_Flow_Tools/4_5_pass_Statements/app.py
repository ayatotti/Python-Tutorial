# -*- coding: UTF-8 -*-

# > The pass statement does nothing.
# > It can be used when a statement is required syntactically but the program requires no action
print('''\
# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action\
''')
#while True:
#        pass # Busy-wait for kerboard interrupt (Ctrl+C)
#
# Traceback (most recent call last):
#  File "app.py", line 10, in <module>
#            pass # Busy-wait for kerboard interrupt (Ctrl+C)

print()

# > This is commonly used for creating minimal classes:
print('This is commonly used for creating minimal classes:')
class MyEmptyClass:
        pass

print()

# > Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level.
# > The pass is silently ignored:
print('''\
# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level.
# The pass is silently ignored:\
''')
def initlog(*args):
        pass # Remember to implement this!

