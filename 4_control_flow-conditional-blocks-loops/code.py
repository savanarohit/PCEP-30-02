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

# Joining Multiple Conditions using and , or and not
# Boolean Operators Priority
# 1. NOT
# 2. AND
# 3. OR


# Example - and  (Both condition should be True)
user_age = int(input("Enter your age: "))
user_country = input("Enter your country name: ")

if user_age < 25 and user_country == "India":
    print("You can apply for a India student exchange programme")
else:
    print("Sorry, you do not qualify")

# Example - or (Any one condition should be True)
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

# Example with all - and , or and not
user_age = int(input("Enter you age: "))
user_country = input("Enter you country name: ")

if (
    not user_country == "India"
    and user_age < 25
    or user_country == "USA"
    and user_age < 20
):
    print("You qualify")
else:
    print("You don't qualify")

# Nested if statements
answer_a = input("Do you like traveling y/n: ")
if answer_a == "y":
    answer_b = input("And do you like Asia? y/n: ")
    if answer_b == "y":
        print("Excellent: You can win a ticket to Thailand: ")
    else:
        print("Sorry to hear that: ")
else:
    print("Sorry to hear that: ")


# While loop in Python allows you to repeatedly execute a block of code as long as a certain condition is true. It's useful when you want to perform a task repeatedly until a specific condition is met.
count = 1
while count < 10:
    count += 1
    print(count)

# Example - Secret Number guess game
secret_number = 15
user_input = int(input("Enter a number between 10 to 20: "))
while user_input != secret_number:
    print("Wrong")
    user_input = int(input("Try to guess the secret number from 10 to 20: "))
print("Perfect! You have guessed the secret number:")


# For loop is a control flow statement that allows you to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It repeatedly executes a block of code for each item in the sequence until all items have been processed

# Example 1
fruits = ["apple", "orange", "grapefruit"]

for f in fruits:
    print(f)

# Example 2
for counter in range(5):
    print(counter)

# Example 3
for counter in range(1, 5):
    print(counter)

# Example 4
# the last number 2 is increment value
for counter in range(1, 10, 2):
    print(counter)


# Break statement is used to exit a loop prematurely. It allows you to terminate the execution of a loop before it has completed all its iterations. When the break statement is encountered, the control flow immediately exits the loop, and the program continues with the next statement after the loop.

bookshelf = ["fiction", "science", "biography", "history", "poetry"]

for shelf in bookshelf:
    if shelf == "biography":
        print("Found the book in the", shelf, "section!")
        break
    else:
        print("Searching in the", shelf, "section...")

print("End of search.")


# Continue statement is used to skip the remaining code within a loop iteration and proceed to the next iteration. When the continue statement is encountered, it immediately jumps to the next iteration without executing any further code within the loop for the current iteration.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Pass
for i in range(11):
    pass  # Loop, If , elif and else requires at least one instruction inside it's body

# Nested Loop is a loop inside another loop. It allows you to create complex iterations by nesting one loop inside another. The inner loop is executed for each iteration of the outer loop.

primary_colors = ["red", "blue", "yellow"]
secondary_colors = ["orange", "green", "purple"]

for primary_color in primary_colors:
    for secondary_color in secondary_colors:
        print(primary_color, "and", secondary_color)


# Loops with else statement
i = 5
while i < 5:
    print(i)
    i += 1
    break
else:
    print("else:", i)
