
students = {}

n = input("Enter number of students (1-100): ").strip()

if n.isdigit() and 1 <= int(n) <= 100:
    n = int(n)

    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Enter name: ").strip()
        age = input("Enter age: ").strip()
        student_class = input("Enter class: ").strip()
        roll_no = input("Enter roll number: ").strip()
        marks = input("Enter marks: ").strip()

        if not name or not student_class:
            print("Name and class cannot be empty.")
            continue

        if not age.isdigit() or not roll_no.isdigit():
            print("Age and roll number must be whole numbers.")
            continue

        if not marks.replace(".", "", 1).isdigit():
            print("Marks must be numeric.")
            continue

        age = int(age)
        roll_no = int(roll_no)
        marks = float(marks)

        if age <= 0 or age > 120 or roll_no <= 0 or marks < 0 or marks > 100:
            print("Invalid age, roll number, or marks.")
            continue

        if roll_no in students:
            print("Roll number already exists.")
            continue

        students[roll_no] = {
            "name": name,
            "age": age,
            "class": student_class,
            "marks": marks
        }

    print("\nStudent Records:")
    print(students)

else:
    print("Enter a whole number between 1 and 100.")