# single line output using print() function
print("Hello World!")

# Multiline output using print() function
print("Hello", "World!")
print(
    """Hello World this
      is multiline text"""
)

# Test - Let's practice the print() function. Show the following message to the output:

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
