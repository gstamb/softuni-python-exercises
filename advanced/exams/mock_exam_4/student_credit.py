def students_credits(*args):
    """
    Calculates the credits earned by a student based on an input of variable length.
    :param args: receives a variable number of arguments in the format:
                                                    "{course name}-{credits}-{max test points}-{diyan's points}
    :return: a string containing information about currently progress toward achieving the target credits of 240
    and a breakdown of credits earned in each course
    """
    courses_and_credits = {}
    target_credits = 240
    # loops over the arguments and collects the course name and credits earned
    for course in args:
        course_name, maximum_credits, max_possible_test_pts, students_test_pts = course.split("-")

        # credits are proportional to score
        credits_earned = int(maximum_credits) * (int(students_test_pts) / int(max_possible_test_pts))
        if course_name not in courses_and_credits:
            courses_and_credits[course_name] = credits_earned

    result_string = ""
    sum_credits_earned = sum(courses_and_credits.values())
    # builds and forms a return string with sorted data
    if target_credits <= sum_credits_earned:
        result_string += f"Diyan gets a diploma with {sum_credits_earned:.1f} credits.\n"
    else:
        result_string += f"Diyan needs {target_credits - sum_credits_earned:.1f} credits more for a diploma.\n"

    for course, credits in sorted(courses_and_credits.items(), key=lambda x: -x[1]):
        result_string += f"{course} - {credits:.1f}\n"

    return result_string


def main():
    """ The program calculates whether a student has collected enough credit to graduate"""
    print(
        students_credits(
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Java Development-10-300-150"
        )
    )


if __name__ == "__main__":
    main()
