def calculator():

    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

        num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()

        try:
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
        if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    else:
        print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
    calculator()



