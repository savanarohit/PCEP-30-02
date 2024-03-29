# # single line output using print() function
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

# Example - Store daily sales data in variables. Then get the Average weekly Sales number
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

# Comments in Python - Hash can be used for single line comment and Triple quote can be used for multiline comment
# Single Line comment

"""MultiLine
   comment
"""

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

# Operators - Operators are special symbols that perform operations on values or variables. They are used to manipulate data, perform calculations, compare values, and control program flow. Python supports a wide range of operators, including arithmetic operators, comparison operators, logical operators, bitwise operators, assignment operators, membership operators, and identity operators.
#  Arithmetic Operators - To perform Mathematic operations
a = 20
b = 15
c = 30.5

# Addition (+)
print(a + b)

# Subtraction (-)
print(c - a)

# Multiplication (*)
print(a * b)

# Division (/)
print(a / b)

# Exponent (**)
print(a**b)

# Modulus (%)
print(a % b)

# Floor Division (//)
print(a // b)

# String Operator

# (*) For replication
print("Python\n" * 3)
print("4\n" * 3)

# (+) For String Concatenation - Combining two or more strings
x = "First string"
y = "Second string"
z = x + y

print("Combined String is:", (z))
print("Combined String is:", x + y)  # Always use ,
print("Combined String is:" + x + y)

# Reassigning values - Reassigning values in Python refers to the process of changing the value associated with a variable
# Define a variable and assign an initial value
x = 5
print("Initial value of x", x)

# Reassign a new value of the variable
x = 10
print("New value of x", x)

# Input() Function - the input() function is used to prompt the user for input from the keyboard. It reads the user's input as a string and returns that value
name = input("Please enter your name:")
print("Hello, " + name + " !How can I assist you today?")
