# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calc_average(numbers):
    if len(numbers) == 0:
        return 0
    return calc_sum(numbers) / len(numbers)


def calc_max(numbers):
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def calc_min(numbers):
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


if __name__ == "__main__":
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: Please enter a positive number.")
    else:
        numbers_list = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            numbers_list.append(val)

        print("\nResults:")
        print(f"Sum:     {calc_sum(numbers_list)}")
        print(f"Average: {calc_average(numbers_list)}")
        print(f"Maximum: {calc_max(numbers_list)}")
        print(f"Minimum: {calc_min(numbers_list)}")