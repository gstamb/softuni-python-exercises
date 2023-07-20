courses = input().split(", ")

while True:
    action = input()

    if action == "course start":
        break
    elif action.startswith("Add"):
        _, course = action.split(":")
        if course not in courses:
            courses.append(course)
    elif action.startswith("Insert"):
        _, course, index = action.split(":")
        if course not in courses:
            courses.insert(int(index), course)
    elif action.startswith("Remove"):
        _, course = action.split(":")
        if course in courses:
            courses.remove(course)

        course_exercise = course + "-Exercise"

        if course_exercise in courses:
            courses.remove(course_exercise)


    elif action.startswith("Swap"):
        _, course, target_course = action.split(":")
        if course in courses and target_course in courses:
            course_index = courses.index(course)
            target_course_index = courses.index(target_course)
            courses[course_index], courses[target_course_index] = courses[target_course_index], courses[course_index]

        course_exercise = course + "-Exercise"
        target_course_exercise = target_course + "-Exercise"

        if course_exercise in courses:
            courses.remove(course_exercise)
            courses.insert(target_course_index + 1, course_exercise)

        if target_course_exercise in courses:
            courses.remove(target_course_exercise)
            courses.insert(course_index + 1, target_course_exercise)

    elif action.startswith("Exercise"):
        _, course = action.split(":")
        if course in courses:
            index_course = courses.index(course)
            courses.insert(index_course + 1, course + "-Exercise")
        else:
            courses.append(course)
            courses.append(course + "-Exercise")

for index, value in enumerate(courses):
    print(f"{index + 1}.{value}")
