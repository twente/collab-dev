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

# TODO: ADD a function to select between division and multiplication here.
# TODO: Add comments/docstrings to code
# TODO: Fix bug in function in operations.py
# TODO: Write documentation
# TODO: Write tests for functions
# TODO: Update README.md
# TODO: Add other operations to operations.py
# TODO: Select and add license to repo
# TODO: Update the citation file with collaborator's names
# TODO: Write collaboration guidelines
