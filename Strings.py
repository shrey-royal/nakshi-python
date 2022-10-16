'''
What is a string?
A string is a sequence of characters. You can use single quotes or double quotes to represent strings.

1 - String Indexing
    a - positive indexing
    b - negative indexing
2 - String Slicing
    a - positive slicing
    b - negative slicing
3 - String Methods
    a-z

'''

# mystring = "Hello World!"
          # 01234567891011
# print(mystring)
# print(len(mystring))

# String Indexing -> positive indexing
# Index starts at 0
# print(mystring[0]) # H
# print(mystring[8])


# indexing takes 3 different arguments -> start, stop, step
# start -> where to start the slice
# stop -> where to end the slice -> stop is not included in the slice
# step -> how many characters to skip -> default is 1


# print(mystring[0:5])
# print(mystring[6:11])
# print(mystring[4:8])
# print(mystring[0:12:1])
# print(mystring[::1])

# String Indexing -> negative indexing

# print(mystring[-1])
# print(mystring[-2])
# print(mystring[-12])

# 0 1 2 3 4 5 6 7 8 9 10 11   -> positive indexing
# H E L L O   W O R L D  !    -> string


# H    E    L    L    O    W    O    R    L    D    !    -> string
# -12 -11  -10  -9   -8   -7 -6 -5  -4   -3    -2   -1  -> negative indexing

# world -> negative indexing
# print(mystring[-6:-1:1])
# print(mystring[-6:-1:2])

'''
Tasks:- 

1. Write a program to print the string in reverse order.
2. Write a program to print the string in reverse order with a step of 2.

'''

# string methods
mystring = "Hello World!, I am a Python Developer"
print(mystring)
print(len(mystring))

# 1. capitalize() -> capitalize the first letter of the string
# print(mystring.capitalize())

# 2. casefold() -> convert the string into lower case
# print(mystring.casefold())

# 3. center() -> center align the string
# print(mystring.center(50, "#"))

# 4. count() -> count the number of times a substring occurs in the string
# print(mystring.count("o"))

