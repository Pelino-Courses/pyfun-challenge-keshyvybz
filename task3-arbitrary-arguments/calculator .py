"""

this is a command line calculator that accepts number of inputs and operations frmo the user.
this will be this operations:addition,substraction,multiply, divide, power, modulo.

 Ex:
calculate(10, 5, add=True, divide=True)
add: 15,divide: 2.0}
"""
def add(*args):
    """Return the sum of all arguments"""
    return sum(args)

def subtract(*args):
    """Return the result of subtracting all arguments."""
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Return the product of all arguments."""
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Return the result of dividing the first argument by the rest."""
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result /= num
    return result

def power(*args):
    """Raise the first number to the power of the second, third, etc."""
    result = args[0]
    for num in args[1:]:
        result = result ** num
    return result

def modulo(*args):
    """Apply modulo operation from left to right."""
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        result %= num
    return result

def process_operations(*args, **kwargs):
    """
   do the required operation on specific argunment 

    Parameters:
    *args: Numeric inputs (int or float).
    **kwargs: Operations to apply as booleans.

    Returns:
    dict: operation names and results.

    Raises:
    ValueError: If input types are invalid or unsupported operations are specified.
    """
    if not args:
        raise ValueError("At least one number must be provided.")

    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All inputs must be integers or floats.")

    supported_operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power,
        'modulo': modulo
    }

    results = {}
    for op_name, do_op in kwargs.items():
        if op_name not in supported_operations:
            raise ValueError(f"Unsupported operation: '{op_name}'. Supported operations are: {list(supported_operations)}")
        if do_op:
            results[op_name] = supported_operations[op_name](*args)

    return results

def calculate(*args, **kwargs):
    """
    Main interface for the calculator.

    Parameters:
    *args: Numbers to calculate with.
    **kwargs: Operations to perform (e.g., add=True, divide=True)

    Returns:
    dict: Dictionary of operation results.

    Example:
    calculate(10, 5, add=True, divide=True)
    add': 15, 'divide': 2.0
    """
    return process_operations(*args, **kwargs)

# Demonstration block
if __name__ == "__main__":
    try:
        results = calculate(10, 2, add=True, subtract=True, multiply=True, divide=True, power=True, modulo=True)
        for op, value in results.items():
            print(f"{op.title()}: {value}")
    except Exception as e:
        print("Error:", e)
