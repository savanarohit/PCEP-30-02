# single line output using print() function
print("Hello World!")

# Multiline output using print() function
print("Hello", "World!")
print(
    """Hello World this
      is multiline text"""
)

# Example - Using print() Show the following message to the output:

# I'm learning to become a Python developer!
# I'm so excited!

# Remember that the second sentence must appear on a separate line.
# Remember that any typo in your solution will make it marked as incorrect.

print("I'm learning to become a Python developer!\nI'm so excited!")


# Variable - a variable is a reserved memory location to store data values that can be modified during the execution of a program. The name of a variable is used to access its stored value.

# Example - Store daily sales data in variables.Then get Average weekly Sales number
DAY1_SALES = 10
DAY2_SALES = 15
DAY3_SALES = 18
DAY4_SALES = 20
DAY5_SALES = 13

TOTAL_SALES = DAY1_SALES + DAY2_SALES + DAY3_SALES + DAY4_SALES + DAY5_SALES
AVG_WEEKLY_SALES = TOTAL_SALES / 5
print(AVG_WEEKLY_SALES)

# Data Types - data types are categories of values that determine how they can be used and manipulated. There are several built-in data types in Python, including integers, floats, strings, booleans, lists, tuples, and dictionaries.

# Example

# Int
AGE = 25
print(type(AGE))

# Floats
WEIGHT = 65.4
print(type(WEIGHT))

# String
NAME = "Robbin"
print(type(NAME))

# Booleans
IN_STOCK = True
print(type(IN_STOCK))

# Lists
grocery_list = ["milk", "eggs", "bread"]
print(type(grocery_list))

# Tuples
coordinates = (52.345, -1.2345)
print(type(coordinates))

# Dictionaries
customer = {"name": "John Doe", "age": "25", "email": "johndoe@example.com"}
print(type(customer))


# Comments in Python

# Hash can be used for single line comment
# Triple quote can be used for multiline comment

# Numerical Representations in Python

# Integers
x = 5
print(type(x))

# Floating-point Numbers
x = 2.0
print(type(x))

# Complex Numbers
z = 2 + 3j
print(type(z))

# Scientific notation
print(4e10)
print(type(4e10))

# Scientific notation for small numbers
print(0.0000000004)

# Octal numbers - octal numbers are represented using the prefix 0o or 0O, followed by a sequence of octal digits (0-7).
x = 0o10
print(x)
print(type(x))

# hexadecimal numbers - hexadecimal numbers are represented using the prefix 0x or 0X, followed by a sequence of hexadecimal digits (0-9 and A-F or a-f).
x = 0x1A
print(x)


# Operators - Python
