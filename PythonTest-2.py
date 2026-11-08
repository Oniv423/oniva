def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please choose +, -, *, or /.")
            return
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    calculator()
