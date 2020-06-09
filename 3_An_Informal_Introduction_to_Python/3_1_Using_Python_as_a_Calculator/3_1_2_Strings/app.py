# -*- coding: UTF-8 -*-

# > Besides numbers, Python can also manipulate strings,
# > which can be expressed in several ways.
# > They can be enclosed in single quotes ('...') or double quotes ("...") with the same result.
# > \ can be used to escape quotes:
print('# Besides numbers, Python can also manipulate strings,\n# which can be expressed in several ways.\n# They can be enclosed in single quotes (\'...\') or double quotes ("...") with the same result.\n# \ can be used to escape quotes:')
print('spamm eggs') # single quotes
print('doesn\'t') # use \' to escape the single quotes...
print("doesn't") # or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

print()

# > In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes.
# > While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent.
# > The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.
# > The print() function produces a more readable output,
# > by omitting the enclosing quotes and by printing escaped and special characters

# > If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:')
print('C:\some\name') # here \n means newline
print(r'C:\some\name') # note the r before the quote

print()

# > String literals can span multiple lines.
# > One way is using triple-quotes: """...""" or '''...'''.
# > End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.
print('''\
# String literals can span multiple lines.
# One way is using triple-quotes: """...""" or \'\'\'...\'\'\'. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.\
''')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print()

# > Strings can be concatenated (glued together) with the + operator, and repeated with *:
print('# Strings can be concatenated (glued together) with the + operator, and repeated with *:')
print(3 * 'un' + 'ium') # 3 times 'un', followed by 'ium'

print()

# > Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.')
print('Py' 'thon') # 'Python'

print()

# > This feature is particularly useful when you want to break long strings:
print('# This feature is particularly useful when you want to break long strings:')
text = ('Put several strings within parentheses '
    'to have them joined together.')
print(text) # Put several strings within parentheses to have them joined together.

print()

# > This only works with two literals though, not with variables or expressions.
# > If you want to concatenate variables or a variable and a literal, use +:
print('''\
# This only works with two literals though, not with variables or expressions:
# If you want to concatenate variables or a variable and a literal, use +:\
''')
prefix = 'Py'
#prefix 'thon'  # can't concatenate a variable and a string literal
#  File "app.py", line 72
#    prefix 'thon'
#                ^
#SyntaxError: invalid syntax

#('un' * 3) 'ium'
#  File "app.py", line 78
#    ('un' * 3) 'ium'
#                   ^
#SyntaxError: invalid syntax

print(prefix + 'thon') # Python

print()

# > Strings can be indexed (subscripted), with the first character having index 0.
# > There is no separate character type; a character is simply a string of size one:
print('''\
# Strings can be indexed (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one:\
''')
word = 'Python'
print(word[0]) # P
print(word[5]) # n

print()

# > Indices may also be negative numbers, to start counting from the right:
print('''\
# Indices may also be negative numbers, to start counting from the right:
# Note that since -0 is the same as 0, negative indices start from -1.\
''')
print(word[-1]) # n # last character
print(word[-2]) # o # second-last character
print(word[-6]) # P

print()

# > In addition to indexing, slicing is also supported.
# > While indexing is used to obtain individual characters, slicing allows you to obtain substring:
print('''\
# In addition to indexing, slicing is also supported.
# While indexing is used to obtain individual characters, slicing allows you to obtain substring:\
''')
print(word[0:2]) # Py # characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # tho  # characters from position 2 (included) to 5 (excluded)

# > Note how the start is always included, and the end always excluded.
# > This makes sure that s[:i] + s[i:] is always equal to s:
print('# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:')
print(word[:2] + word[2:]) # Python

# > Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print('# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.')
print(word[:2]) # Py # character from the beginning to position 2 (excluded)
print(word[4:]) # on # characters from position 4 (included) to the end
print(word[-2:]) # on # characters from the second-last (included) to the end

# > One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0.
# > Then the right edge of the last character of a string of n characters has index n, for example:
# > The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices.
# > The slice from i to j consists of all characters between the edges labeled i and j, respectively.
# > For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds.
# > For example, the length of word[1:3] is 2.
print('''\
# One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0.
# Then the right edge of the last character of a string of n characters has index n
# The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices.
# The slice from i to j consists of all characters between the edges labeled i and j, respectively.
# For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds.
# For example, the length of word[1:3] is 2.\
''')
print('''\
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1\
''')

# > Attempting to use an index that is too large will result in an error:
print('# Attempting to use an index that is too large will result in an error:')
#word[42]  # the word only has 6 characters
#Traceback (most recent call last):
#  File "app.py", line 155, in <module>
#IndexError: string index out of range

# > However, out of range slice indexes are handled gracefully when used for slicing:
print('# However, out of range slice indexes are handled gracefully when used for slicing:')
print(word[4:42]) # 'on'
print(word[42:]) # ''

# > Python strings cannot be changed — they are immutable.
# > Therefore, assigning to an indexed position in the string results in an error:
#word[0] = 'J'
#Traceback (most recent call last):
#  File "app.py", line 167, in <module>
#    word[0] = 'J'
#TypeError: 'str' object does not support item assignment
#word[2:] = 'py'
#Traceback (most recent call last):
#  File "app.py", line 172, in <module>
#    word[2:] = 'py'
#TypeError: 'str' object does not support item assignment

# > If you need a different string, you should create a new one:
print('# If you need a different string, you should create a new one:')
print('J' + word[1:]) # 'Jython'
print(word[:2] + 'py') # 'Pypy'

print()

# > The built-in function len() returns the length of a string:
print('# The built-in function len() returns the length of a string:')
s = 'supercalifragilisticexpialidocious'
print(len(s)) # 34