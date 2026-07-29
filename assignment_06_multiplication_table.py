# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_table(n):
    """
    Prints the multiplication table for a given number 'n' from 1 to 12.
    """
    print(f"Multiplication Table for {n}:")
    for i in range(1, 13):
        print(f"{n} x {i:<2} = {n * i}")


def single_table():
    """
    PART A: Prompts the user for a single number and prints its table.
    """
    user_input = input("Enter a positive integer for Part A: ")

    if not user_input.isdigit() or int(user_input) <= 0:
        print("Error: Please enter a valid positive integer.")
        return

    number = int(user_input)
    print_table(number)


def multiple_tables():
    """
    PART B (Bonus): Prompts for a number N and prints all tables from 1 to N.
    """
    user_input = input("Enter N (positive integer) for Part B: ")

    if not user_input.isdigit() or int(user_input) <= 0:
        print("Error: Please enter a valid positive integer.")
        return

    n = int(user_input)
    for i in range(1, n + 1):
        print_table(i)
        if i < n:
            print("-" * 27)


def main():
    """
    Main function to run both parts of the assignment.
    """
    print("=== PART A: Single Table ===")
    single_table()

    print("\n=== PART B: Tables from 1 to N ===")
    multiple_tables()


if __name__ == "__main__":
    main()