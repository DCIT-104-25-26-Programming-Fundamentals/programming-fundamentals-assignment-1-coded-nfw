# =============================================================================
# display_menu():
def display_menu():
    """Displays the main menu options."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU   ")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """Helper function to calculate the average of a list of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def add_student(students):
    """Prompts for student details and appends a dictionary to the list."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    # Check for duplicate ID
    for student in students:
        if student["id"] == student_id:
            print(f"Error: A student with ID '{student_id}' already exists.")
            return

    # Ask for number of scores with validation
    num_scores_input = input("How many scores? ").strip()
    if not num_scores_input.isdigit() or int(num_scores_input) <= 0:
        print("Error: Number of scores must be a positive integer.")
        return

    num_scores = int(num_scores_input)
    scores = []

    # Collect individual scores
    for i in range(1, num_scores + 1):
        while True:
            score_input = input(f"Enter score {i}: ").strip()
            try:
                score = float(score_input)
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric score.")

    # Create dictionary and store in list
    student_record = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student_record)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Displays all student records in a formatted table."""
    if not students:
        print("No student records found.")
        return

    print("-" * 60)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<15} {'Average':<8}")
    print("-" * 60)

    for student in students:
        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else f"{s:.1f}" for s in student["scores"]
        )
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<20} {student['id']:<12} {scores_str:<15} {avg:<8.2f}")

    print("-" * 60)


def calculate_student_average(students):
    """Finds a student by ID and prints their average score."""
    if not students:
        print("No student records found.")
        return

    target_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == target_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID '{target_id}' not found.")


def main():
    """Main program execution loop."""
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()