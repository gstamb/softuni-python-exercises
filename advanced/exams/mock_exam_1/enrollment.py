def gather_credits(*args):
    """ Function that receives a target number of credits for graduation and a sequence of courses.
        The courses container name and number of credits
        Function will enroll courses until the required amount of credits is reached.
        Courses can only be enrolled into once.
     """
    required_credits = args[0]
    courses = args[1:]
    current_credits = {"collected": 0, "courses": []}
    for course in courses:
        name, course_credits = course
        if current_credits["collected"] < required_credits:
            if name not in current_credits["courses"]:
                current_credits["collected"] += course_credits
                current_credits["courses"].append(name)
            else:
                continue
        else:
            break
    if current_credits["collected"] >= required_credits:
        return f"Enrollment finished! Maximum credits: {current_credits['collected']}.\n" \
               f"Courses: {', '.join(sorted(current_credits['courses'], key=lambda x: x))}"

    else:
        return (
            f"You need to enroll in more courses! You have to gather"
            f" {required_credits - current_credits['collected']} credits more.")


def main():
    print(gather_credits(
        60,
        ("Basics", 27),
        ("Fundamentals", 27),
        ("Advanced", 30),
        ("Web", 30)
    ))


if __name__ == "__main__":
    main()
