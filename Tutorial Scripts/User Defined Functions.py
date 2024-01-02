# How a user can define their own custom Functions


# Simple function
print("1. Simple Function:")


def greet_user(name):
    """A simple function to greet the user"""
    print("Hello, " + name + "!")


# Function call
greet_user("Rohit")


# Function with parameters
print("2. Function with Parameters:")


def add_numbers(a, b):
    """A function that adds two numbers."""
    result = a + b
    return result


# Function call with parameters
sum_result = add_numbers(5, 7)
print("Sum:", sum_result)  # As function is not printing we need to print explicitly

# Default parameters
print("3. Default Parameters:")


def greet(name, greeting="Hello"):
    """A function with a default parameter."""
    print(greeting + ", " + name + "!")


# Section 7: Function call with default parameter
greet("Bob")
greet("Charlie", "Hi")
