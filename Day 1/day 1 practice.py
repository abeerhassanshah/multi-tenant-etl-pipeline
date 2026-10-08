n = int(input("Enter number of students:"))

students = {}

for i in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    student_class = input("Enter class:")
    roll_no = input("Enter roll number:")
    marks = float(input("Enter marks:"))

    students[roll_no] = {
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks
    }

print("\nStudent Records:")
print(students)
