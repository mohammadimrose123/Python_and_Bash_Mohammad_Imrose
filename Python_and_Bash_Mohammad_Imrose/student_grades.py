student_grades = {
    "Rahul": "A",
    "Priya": "B",
    "Arjun": "C"
}

print("Initial student grades:")
for name, grade in student_grades.items():
    print(name, ":", grade)

print("\nAdding a new student...")
name = input("Enter new student name: ")
grade = input("Enter grade: ")

if name in student_grades:
    print("Student already exists.")
else:
    student_grades[name] = grade
    print("Student added successfully.")

print("\nUpdating a student...")
update_name = input("Enter student name to update: ")
if update_name in student_grades:
    new_grade = input("Enter new grade: ")
    student_grades[update_name] = new_grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

print("\nAll student grades:")
for name, grade in student_grades.items():
    print(name, ":", grade)
