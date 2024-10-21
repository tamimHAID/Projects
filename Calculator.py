# Get inputs from the user
num1 = float(input("Insert a number: "))
variable = input("Insert a variable (+, -, *, /): ")
num2 = float(input("Insert a number: "))

# Perform calculations
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

# Check for division by zero
if num2 != 0:
    divide = num1 / num2
else:

    divide = "Error: Division by zero!"

# Check the variable and perform the operation
if variable == "+":
    print(add)
elif variable == "-":
    print(subtract)
elif variable == "*":
    print(multiply)
elif variable == "/":
    if num2 != 0:
        print(divide)
    else:
        print("Error: Division by zero!")
else:
    print("Error: Invalid input")
