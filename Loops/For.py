'''
For Loop :- 

Entry controlled loop as the condition of the for loop is checked before the body gets executed.
The for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.


Syntax :-

for val in sequence:
    Body of for

# Here val is the variable that takes the value of the item inside the sequence on each iteration.


'''


# Example 1 :-

# for i in "Hello_World":
#     print(i)


# Example 2 :-

for i in range(2, 51):
    print(i)

# range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# range(start, stop, step)


'''
Make a python Program that scans 2 numbers from the user (start, stop) and print all the numbers between them.
'''