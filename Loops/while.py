'''
# while loop
while condition:
    body of while

'''

# Example 1 :-

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Example 2 :-

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1


# Task :- Make a program to find the power of a number using while loop.

num = int(input("Enter the number : "))
power = int(input("Enter the power : "))
result = 1

while power > 0:
    result *= num
    power -= 1

print(result)