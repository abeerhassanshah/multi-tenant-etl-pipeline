
MIN_STUDENTS = 1
MAX_STUDENTS = 100

MIN_AGE = 18
MAX_AGE = 40

MIN_MARKS = 0
MAX_MARKS = 100

MAX_NAME_LENGTH = 49


def valid_name(full_name):
    return (
        0 < len(full_name) <= MAX_NAME_LENGTH
        and not any(char.isdigit() for char in full_name)
    )


def valid_roll_number(roll_number):
    return (
        bool(roll_number)
        and roll_number[0].isalnum()
        and roll_number[-1].isalnum()
        and all(char.isalnum() or char == "-" for char in roll_number)
    )


def get_students(number_of_students):
    students = {}

    for _ in range(number_of_students):
        while True:
            full_name = input("Full name: ").strip()

            if valid_name(full_name):
                break

            print("Name must be 1-49 characters and contain no digits.")

        while True:
            age_text = input("Age: ").strip()

            if age_text.isdigit() and MIN_AGE <= int(age_text) <= MAX_AGE:
                age = int(age_text)
                break

            print("Age must be a whole number from 18 to 40.")

        student_class = input("Class: ").strip()

        while not student_class:
            print("Class cannot be empty.")
            student_class = input("Class: ").strip()

        while True:
            roll_number = input("Roll number: ").strip().upper()

            if not valid_roll_number(roll_number):
                print("Use letters/numbers and optional internal hyphens.")
                continue

            if roll_number in students:
                print("That roll number already exists.")
                continue

            break

        while True:
            marks_text = input("Marks (0-100): ").strip()

            try:
                marks = float(marks_text)

                if MIN_MARKS <= marks <= MAX_MARKS:
                    break

            except ValueError:
                pass

            print("Marks must be a number from 0 to 100.")

        students[roll_number] = {
            "full_name": full_name,
            "age": age,
            "class": student_class,
            "marks": marks
        }

    return students


def display_students(students):
    print("\nSTUDENT RECORDS")

    for roll_number, details in students.items():
        print(f"\nRoll number: {roll_number}")
        print(f"Full name: {details['full_name']}")
        print(f"Age: {details['age']}")
        print(f"Class: {details['class']}")
        print(f"Marks: {details['marks']}")
