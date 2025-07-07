from art import logo

# Display calculator logo
print(logo)

# Define basic arithmetic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Map operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Main calculator logic
def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        # Display available operations
        for symbol in operations:
            print(symbol)

        # Get operation and next number
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Perform calculation and display result
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask user whether to continue or restart
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 100)
            calculator()

# Start the calculator
calculator()



