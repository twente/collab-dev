'''
Combining operations
'''

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = summation(num1, num2)
    elif operation == "subtract":
        result = subtraction(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose 'add' or 'subtract'.")

    return result

# TODO: create function to select between division and multiplication
# TODO: Add comments/docstrings to code
# TODO: Fix bug in function in operations.py
# TODO: Write documentation
# TODO: Write tests
# TODO: Update README.md

