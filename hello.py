# hello.py
print("--- Simple Python Calculator ---")

try:
    # Get user inputs
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ").strip()
    num2 = float(input("Enter second number: "))

    # Calculate results based on operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error! Division by zero is not allowed."
        else:
            result = num1 / num2
    else:
        result = "Invalid operator!"

    print(f"Result: {result}")

except ValueError:
    print("Error! Please enter valid numbers.")
