# Asks for user input for the numbers and what operation to use
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("What operation would you like to use (+, -, *, /): ")

# Asks for a new 2nd number repeatedly if the equation divides by 0
while operation == "/" and num2 == 0:
    try:
        num2 = float(input("Error. 2nd number must not be 0 when dividing: "))
    except:
        break

# Functions for adding, subtracting, multiplying, and dividing
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

# Calculates based on what operation was given using functions
if operation == "+":
    answer = add(num1, num2)
elif operation == "-":
    answer = subtract(num1, num2)
elif operation == "*":
    answer = multiply(num1, num2)
elif operation == "/":
    answer = divide(num1, num2)

# Prints calculatd answer
print(f"Result: {answer}")
