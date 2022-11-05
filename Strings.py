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

# 5. encode() -> encode the string
# print(mystring.encode())

# 6. endswith() -> check if the string ends with a substring
# print(mystring.endswith("as per"))

# 7. expandtabs() -> expand tabs in the string
# print("Nakshi\tPanchal".expandtabs(100))

# 8. find() -> find the index of the first occurence of a substring
# print(mystring.find("o"))

# 9. format() -> format the string
# print("My name is {} and I am {} years old.".format("Nakshi", 12))

# 10. format_map() -> format the string using a mapping
# print("My name is {name} and I am {age} years old.".format_map({"name": "Nakshi", "age": 12}))

# 11. index() -> find the index of the first occurence of a substring
# print(mystring.index("o"))

# 12. isalnum() -> check if the string is alphanumeric
# print("sdffcfhg6558bh78jn".isalnum())

# 13. isalpha() -> check if the string is alphabetic
# print("sdffcfhg6558bh78jn".isalpha())

# 14. isdecimal() -> check if the string is decimal
# print("123456".isdecimal())

# 15. isdigit() -> check if the string is digit
# print("123456".isdigit())

# 16. isidentifier() -> check if the string is a valid identifier
# print("Nakshi".isidentifier())

# 17. islower() -> check if the string is lower case
# print("nakshi".islower())

# 18. isnumeric() -> check if the string is numeric
# print("123456".isnumeric())

# 19. isprintable() -> check if the string is printable
# print("😎".isprintable())

# 20. isspace() -> check if the string is space
# print(" ".isspace())

# 21. istitle() -> check if the string is title
# print("Nakshi Panchal".istitle())

# 22. isupper() -> check if the string is upper case
# print("NAKSHI".isupper())

# 23. join() -> join the elements of an iterable to the end of the string
# print(" ".join(["Nakshi", "Panchal"]))

# 24. ljust() -> left justify the string
# print("Nakshi".ljust(50, "#"))

# 25. lower() -> convert the string into lower case
# print("NAKSHI".lower())

# 26. lstrip() -> remove leading characters
# print("Nakshi".lstrip("N"))

# 27. maketrans() -> return a translation table to be used in translations
# print("Nakshi".maketrans("N", "P"))

# 28. partition() -> partition the string into 3 parts
# print("I'm Nakshi Panchal".partition("a"))

# 29. replace() -> replace a substring with another substring
# print("Nakshi".replace("N", "P"))

# 30. rfind() -> find the index of the last occurence of a substring
# print("Nakshi".rfind("i"))

# 31. rindex() -> find the index of the last occurence of a substring
# print("Nakshi".rindex("i"))

# 32. rjust() -> right justify the string
# print("Nakshi".rjust(50, "#"))

# 33. rpartition() -> partition the string into 3 parts
# print("I'm Nakshi Panchal".rpartition("a"))

# 34. rsplit() -> split the string at the specified separator, and returns a list
# print("Nakshi Panchal".rsplit(" "))

# 35. rstrip() -> remove trailing characters
# print("Nakshi".rstrip("i"))

# 36. swapcase() -> swap cases, lower case becomes upper case and vice versa
# print(mystring.swapcase())
