# -*- coding: UTF-8 -*-

# > The integer numbers (e.g. 2, 4, 20) have type int,
# > the ones with a fractional part (e.g. 5.0, 1.6) have type float.
print('# The integer numbers (e.g. 2, 4, 20) have type int,\n# the ones with a fractional part (e.g. 5.0, 1.6) have type float.')
print(2 + 2) # = 4
print(50 - 5 * 6) # = 20
print((50 - 5 * 6) / 4) # = 5.0
print(8 / 5) # = 1.6 #  division always returns a floating point number

print()

# > Division (/) always returns a float.
# > To do floor division and get an integer result (discarding any fractional result)
# > you can use the // operator;
# > to calculate the remainder you can use %:
print('# Division (/) always returns a float.\n# To do floor division and get an integer result (discarding any fractional result)\n# you can use the // operator;\n# to calculate the remainder you can use %:')
print(17 / 3) # = 5.666666666666667 # classic division returns float
print(17 // 3) # = 5 # floor division discardsthe fractional part
print(17 % 3) # = 2 # the % operator returns the remainder of the division
print(5 * 3 + 2) # = 17 # result * division + remainder

print()

# > With Python, it is possible to use the ** operator to calculate powers
print('# With Python, it is possible to use the ** operator to calculate powers')
print(5 ** 2) # = 25 # 5 squared
print(2 ** 7) # = 128 # 2 to the power of 7

print()

# > The equal sign (=) is used to assign a value to a variable.
# > Afterwards, no result is displayed before the next interactive prompt:
print('# The equal sign (=) is used to assign a value to a variable.')
width = 20
height = 5 * 9
print(width * height)

print()

# > If a variable is not “defined” (assigned a value), trying to use it will give you an error
print('# If a variable is not “defined” (assigned a value), trying to use it will give you an error')
# n  # try to access an undefined variable
# Traceback (most recent call last):
#  File "app.py", line 43, in <module>
#    n
# NameError: name 'n' is not defined

print()

# > There is full support for floating point; 
# > operators with mixed type operands convert the integer operand to floating point
print('# There is full support for floating point;\n# operators with mixed type operands convert the integer operand to floating point')
print(4 * 3.75 -1) # = 14.0

print()

# > In interactive mode, the last printed expression is assigned to the variable _.
# > This means that when you are using Python as a desk calculator,
# > it is somewhat easier to continue calculations
# tax = 12.5 / 100
# price = 100.50
# price * tax
# price + _
# round(_, 2)
# > This variable should be treated as read-only by the user.
# > Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

# > In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction.
# > Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).
