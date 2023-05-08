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

# Example - Store daily sales data in variables to get average weekly sales number
day1_sales = 10
day2_sales = 15
day3_sales = 18
day4_sales = 20
day5_sales = 13

total_sales = day1_sales + day2_sales + day3_sales + day4_sales + day5_sales
avg_daily_sales = total_sales / 5
print(avg_daily_sales)
