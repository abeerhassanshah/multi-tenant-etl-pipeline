
from helpers import (
    MIN_STUDENTS,
    MAX_STUDENTS,
    get_students,
    display_students
)


def main():
    while True:
        number_text = input(
            f"How many students? ({MIN_STUDENTS}-{MAX_STUDENTS}): "
        ).strip()

        if number_text.isdigit():
            number = int(number_text)

            if MIN_STUDENTS <= number <= MAX_STUDENTS:
                break

        print("Enter a whole number from 1 to 100.")

    students = get_students(number)
    display_students(students)


if __name__ == "__main__":
    main()
