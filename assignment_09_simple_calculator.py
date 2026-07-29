def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """Returns the quotient of a divided by b, rounded to 2 decimal places.

    Returns an error message if b is zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of a divided by b.

    Returns an error message if b is zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Displays the calculator menu."""
    print("\n============================")
    print("       SIMPLE CALCULATOR     ")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number(prompt):
    """Helper function to safely get a numeric input from the user."""
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            # Return an int if there's no fractional part for cleaner output display
            return int(val) if val.is_integer() else val
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            num1 = get_number("Enter first number : ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                symbol = "/"
            elif choice == "5":
                result = modulus(num1, num2)
                symbol = "%"
            elif choice == "6":
                result = power(num1, num2)
                symbol = "**"

            # Print error string or formatted equation
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} {symbol} {num2} = {result}")
        else:
            print("Invalid choice! Please select an option between 1 and 7.")


if __name__ == "__main__":
    main()