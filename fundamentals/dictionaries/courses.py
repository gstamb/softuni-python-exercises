courses = {}

while True:

    entry = input()
    if entry == "end":
        break

    course, student = entry.split(" : ")

    if course in courses:
        courses[course].append(student)
    else:
        courses[course] = []
        courses[course].append(student)

for course_name, registered_students in courses.items():
    print("{0}: {1}\n-- {2}".format(course_name, len(registered_students), "\n-- ".join(registered_students)))
