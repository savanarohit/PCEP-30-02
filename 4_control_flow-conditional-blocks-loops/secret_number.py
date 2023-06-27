print(
    """
========================================      
======== SECRET NUMBER GAME ============
========================================
"""
)
secret_number = 15
user_input = int(input("Enter a number between 10 to 20: "))
while user_input != secret_number:
    print("Wrong")
    user_input = int(input("Try to guess the secret number from 10 to 20: "))
print("Perfect! You have guessed the secret number:")
