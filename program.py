
# Simple Calculator

# Menu
def menu():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not possible."

# Main program
while True:
    menu()
    choice = input("Choose an operation:")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid choice. Please choose a valid option.")

    ans = input("Do you want to continue? (y/n): ").lower()
    if ans not in ['y', 'yes']:
        break
