# -*- coding: UTF-8 -*-

# > If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost.
# > Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead.
# > This is known as creating a script.
# > As your program gets longer, you may want to split it into several files for easier maintenance.
# > You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.

# > To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.
# > Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

# > A module is a file containing Python definitions and statements.
# > The file name is the module name with the suffix .py appended.
# > Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# > For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

# > Now enter the Python interpreter and import this module with the following command:
import fibo

# > This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there.
# > Using the module name you can access the functions:

fibo.fib(100) # 0 1 1 2 3 5 8 13 21 34 55 89
print(fibo.fib2(100)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(fibo.__name__) # fibo

# > If you intend to use a function often you can assign it to a local name:
fib = fibo.fib
fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
