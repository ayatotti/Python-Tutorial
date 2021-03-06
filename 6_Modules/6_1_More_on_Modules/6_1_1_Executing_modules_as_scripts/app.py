# -*- coding: UTF-8 -*-

# > When you run a Python module with
#python fibo.py <arguments>

# > Note If you use docker, use next command instead of 'python fibo.py <arguments>'.
#docker run --rm -it -v $(pwd):/app python:3 python /app/fibo.py <arguments>

# > the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".
# > That means that by adding this code at the end of your module:
#if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))

# > you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

# > If the module is imported, the code is not run:
import fibo
fibo.fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# > This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).
