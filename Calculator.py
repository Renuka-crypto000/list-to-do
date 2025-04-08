# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Display the operation menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
operation = input("Enter choice (1/2/3/4): ")

# Input validation for operation
if operation not in ('1', '2', '3', '4'):
    print("Invalid operation choice.")
else:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform calculation based on user choice
        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

