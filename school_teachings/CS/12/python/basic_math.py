"""
***************** basic math module *****************
This module contains basic mathematical operations such as addition, 
subtraction, multiplication, and division. Each function takes two parameters and 
returns the result of the respective operation. The division function also handles division by zero by printing an error message and returning None.
"""

def add(param1, param2):
    """This function takes two parameters and returns their sum."""
    return param1 + param2

def subtract(param1, param2):
    """This function takes two parameters and returns their difference."""
    return param1 - param2

def multiply(param1, param2):
    """This function takes two parameters and returns their product."""
    return param1 * param2

def divide(param1, param2):
    """This function takes two parameters and returns their quotient."""
    if param2 == 0:
        print("Division by Zero")
        return None
    return param1 / param2


