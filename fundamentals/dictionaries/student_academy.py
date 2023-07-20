students = [input() for x in range(int(input()) * 2)]
top_students = {}

for student in range(0, len(students), 2):
    student_name = students[student]
    grade = float(students[student+1])
    if student_name not in top_students:
        top_students[student_name] = grade
    else:
        avg_grade = (top_students[student_name] + grade) / 2
        top_students[student_name] = avg_grade


for student, grade in top_students.items():
    if grade >= 4.5:
        print(f"{student} -> {grade:.2f}")


