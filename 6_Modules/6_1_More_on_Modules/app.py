# -*- coding: UTF-8 -*-

# > A module can contain executable statements as well as function definitions.
# > These statements are intended to initialize the module.
# > They are executed only the first time the module name is encountered in an import statement.
# > (They are also run if the file is executed as a script.)

# > Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module.
# > Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.
# > On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

# > Modules can import other modules.
# > It is customary but not required to place all import statements at the beginning of a module (or script, for that matter).
# > The imported module names are placed in the importing module’s global symbol table.

# > There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table.
# > For example:
from fibo import fib, fib2
fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

del fib, fib2

# > This does not introduce the module name from which the imports are taken in the local symbol table (so in the example, fibo is not defined).


# > There is even a variant to import all names that a module defines:
from fibo import *
fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

del fib, fib2

# > This imports all names except those beginning with an underscore (_).
# > In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

# > Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

# > If the module name is followed by as, then the name following as is bound directly to the imported module.
import fibo as fib
fib.fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

del fib

# > This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.

# > It can also be used when utilising from with similar effects:
from fibo import fib as fibonacci
fibonacci(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# > Note For efficiency reasons, each module is only imported once per interpreter session.
# > Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).
