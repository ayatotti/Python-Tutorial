# -*- coding: UTF-8 -*-

# > The break statement, like in C, breaks out of the innermost enclosing for or while loop.

# > Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
# > This is exemplified by the following loop, which searches for prime numbers:
print('''\
# The break statement, like in C, breaks out of the innermost enclosing for or while loop.

# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
# This is exemplified by the following loop, which searches for prime numbers:\\\
''')
for n in range(2, 10):
        for x in range(2, n):
                if n % x == 0:
                        print(n, 'equals', x, '*', n//x)
                        break
        else:
                # loop fell through without finding a factor
                print(n, 'is a prime number')
print()

# > When used with a loop, the else clause has more in common with the else clause of a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.
print('# When used with a loop, the else clause has more in common with the else clause of a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.')

print()

# > The continue statement, also borrowed from C, continues with the next iteration of the loop:
print('# The continue statement, also borrowed from C, continues with the next iteration of the loop:')
for num in range(2, 10):
        if num % 2 == 0:
                print('Found an even number ', num)
                continue
        print('Found a number ', num)
