# -*- coding: UTF-8 -*-

# > The most useful form is to specify a default value for one or more arguments.
# > This creates a function that can be called with fewer arguments than it is defined to allow. For example:
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
    
# > This function can be called in several ways:
# > - giving only the mandatory argument: ask_ok('Do you really want to quit?')
ask_ok('Do you really want to quit?')
# > - giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2)
# > - or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

print()

# > This example also introduces the in keyword.
# > This tests whether or not a sequence contains a certain value.

print('y' in ('y', 'ye', 'yes'))

print()

# > The default values are evaluated at the point of function definition in the defining scope, so that
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # will print 5.

print()

# > Important warning:
# > The default value is evaluated only once.
# > This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
# > For example, the following function accumulates the arguments passed to it on subsequent calls:
def f(a, L=[]):
    print('identity of L is ',hex(id(L)), ', and default value is ', L)
    L.append(a)
    return L

print(f(1)) # = [1]
print(f(2)) # = [1, 2]
print(f(3)) # = [1, 2, 3]

print()

# > f you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L=None):
    print('identity of L is ',hex(id(L)), ', and default value is ', L)
    if L is None:
        L=[]
    L.append(a)
    return L

print(f(1)) # = [1]
print(f(2)) # = [2]
print(f(3)) # = [3]

print()