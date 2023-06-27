# Control Flow - In Python, control flow refers to the order in which the statements of a program are executed. It allows you to control the flow of execution based on certain conditions or events. Control flow structures in Python include conditional statements (if-elif-else) and loop statements (for and while loops).

# if statement is used to check whether a certain condition is true or false. If the condition is true, then the code inside the if block is executed, otherwise it is skipped.
X = 5
Y = 10
if X < 10:
    print("True")

# if else statement is an extension of the if statement that allows you to specify an alternative code block to execute if the condition in the if statement is false.
Y = 10
X = 20

if Y > X:
    print("Y is bigger")
else:
    print("X is smaller")

# if elif statement is an extension of the if statement that allows you to specify multiple conditions to check. Once it gets True it will exit from the flow.
X = 5
Y = 10
if X > Y:  # Since it is False it will continue with flow.
    print("X is bigger")
elif X < Y:  # Since it is True it will exit from the flow.
    print("X is smaller")
elif X == Y:  # This block of code does not executed.
    print("X is equal to Y")


# Logical Operators are used to perform logical operations on Boolean values (True or False). There are three logical operators available in Python: and, or, and not. These operators allow you to combine multiple Boolean expressions and evaluate their truth values.

# <
# >
# <=
# >=
# ==
# !=

# Example
password = "abc@123"
userinput = "abc@123"

# Check if the input password is valid or not
if userinput == password:
    print("Password match")
else:
    print("Password not match")


# Joining Multiple Conditions ( and , or , not)

# Example - and    (Both condition should be True)
user_age = int(input("Enter your age: "))
user_country = input("Enter your country name: ")

if user_age < 25 and user_country == "India":
    print("You can apply for a India student exchange programme")
else:
    print("Sorry, you do not qualify")

# Example - or  (Any one condition should be True)
user_age = int(input("Enter you age: "))
user_country = input("Enter your country name: ")

if user_age < 25 or user_country == "India":
    print("You can apply for a India student exchange programme")
else:
    print("Sorry, you do not qualify")

# Example - not (It will negates the boolean value if a condition is True it will turn it to False and vice-versa)
user_country = input("Enter your country name: ")
if not user_country == "India":
    print("You are not from India")
else:
    print("You are from India")
