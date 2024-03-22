def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Welcome to the Command-Line Calculator!")
    print("Supported operations:\nAddition\nsubraction\nmultiplication\ndivision")
    print("Enter 'exit' to quit.")

    while True:
        try:
            num1 = input("Enter the first number: ")
            if num1.lower() == 'exit':
                break
            num1 = float(num1)
            
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operator! Please enter one of '+', '-', '*', '/'.")

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)

            print("Result: ", result)
        except ValueError as ve:
            print("Error:", ve)

if __name__ == "__main__":
    calculator()