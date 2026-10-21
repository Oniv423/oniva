def add_numbers(num1, num2):
    return num1 + num2
def multiply_numbers(num1, num2):
    return num1 * num2
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Multiplication")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        result = add_numbers(number1, number2)
        print(f"\nThe result of addition is: {result}")
    elif choice == '2':
        result = multiply_numbers(number1, number2)
        print(f"\nThe result of multiplication is: {result}")
    else:
        print("\nInvalid choice! Please select either 1 or 2.")
except ValueError:
    print("\nInvalid input! Please enter numerical values.")
