# str1 = "Nakshi"
# print("Original String is " + str1)
# print("n : ", str1.count("n"))

# first_char = str1[0]
# middle_char = str1[int(len(str1)/2)]
# last_char = str1[-1]

# print(first_char + middle_char + last_char)

# Write a program to count occurrences of all characters within a string


'''
Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of string
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
'''

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print("Original list of string")
print(str_list)

for i in str_list:
    if i == "":
        str_list.remove(i)

print("After removing empty strings")
print(str_list)