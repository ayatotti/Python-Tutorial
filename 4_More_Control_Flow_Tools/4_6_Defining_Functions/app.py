# -*- coding: UTF-8 -*-

# > We can create a function that writes the Fibonacci series to an arbitrary boundary:
def fib(n): # write Fibonacci series up to n
    '''Print a Fibonacci series up to n.'''
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000) # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,

# > The keyword def introduces a function definition.
# > It must be followed by the function name and the parenthesized list of formal parameters.
# > The statements that form the body of the function start at the next line, and must be indented.

#def functionName(parameters):
#    function body

# > The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring.
# > (More about docstrings can be found in the section Documentation Strings.)
# > There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it.

#def functionName(parameters):
#    '''This is a docstring.'''
#    function body

# > The execution of a function introduces a new symbol table used for the local variables of the function.
# > More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names.
# > Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

global_a, global_b = 10, 20
print('a:', global_a, ' b:', global_b) # a: 10  b: 20

def fib_global(n): # write Fibonacci series up to n
    '''Print a Fibonacci series up to n.'''
    global global_a # use global statement
    global_a, global_b = 0, 1 
    # global_a is global variables. global_b is local variables
    while global_a < n:
        print(global_a, end=',')
        global_a, global_b = global_b, global_a+global_b
    print()

fib_global(2000) # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,
print('a:', global_a, ' b:', global_b) # a: 2584  b: 20
print()

# > The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object).
# > When a function calls another function, a new local symbol table is created for that call.

def print_list(l):
    '''Print list items'''
    l.append(5)
    for i in l:
        print(i, end=',')
    print()

items = [0, 1, 2, 3, 4]
print_list(items) # 0,1,2,3,4,5,
print(items) # [0, 1, 2, 3, 4, 5]

print()

# > A function definition introduces the function name in the current symbol table.
# > The value of the function name has a type that is recognized by the interpreter as a user-defined function.
# > This value can be assigned to another name which can then also be used as a function.
# > This serves as a general renaming mechanism:
print(fib) # <function fib at 0x0123456789ab>
f = fib
f(100) # 0,1,1,2,3,5,8,13,21,34,55,89,
print(f) # <function fib at 0x0123456789ab>

print()

# > Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value.
# > In fact, even functions without a return statement do return a value, albeit a rather boring one.
# > This value is called None (it’s a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the only value written.
# > You can see it if you really want to using print():
fib(0)
print(fib(0)) # None

print()

# > It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
def fib2(n):
    '''Return a list containing the Fibonacci series up to n.'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) # see below
        a, b = b, a + b
    return result

f100 = fib2(100) # call it
print(f100) # = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # write the result

print()

# > This example, as usual, demonstrates some new Python features:

# > - The return statement returns with a value from a function.
# > return without an expression argument returns None. Falling off the end of a function also returns None.
def returnNone():
    return
print(returnNone()) # None

print()

# > - The statement result.append(a) calls a method of the list object result.
# > A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type.
# > Different types define different methods. Methods of different types may have the same name without causing ambiguity.
# > (It is possible to define your own object types and methods, using classes, see Classes) The method append() shown in the example is defined for list objects; it adds a new element at the end of the list.
# > In this example it is equivalent to result = result + [a], but more efficient.
print([0,0,1,2].count(0)) # = 2
print('string'.count('s', 1, 5)) # = 0