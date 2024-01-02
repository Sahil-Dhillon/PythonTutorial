# Conditionals

print("How conditional statements work in Python.")

# Simple if statement
age = int(input("Enter your age: "))  # Convert input to an integer
if age >= 13:
    print("You are a teenager.")

# If-else statement
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# if-elif-else statement
temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("It's freezing cold!")
elif 0 <= temperature <= 20:
    print("The weather is cool.")
else:
    print("It's quite warm outside.")

# Nested conditions
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:  # Modulo Operator check for remainder after dividing by 2
        print("The number is even.")
    else:
        print("The number is odd.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

