def age_assignment(*args, **kwargs):
    """
    Connects a list of names with their corresponding ages using the provided key-value pairs.

    :param args Positional arguments containing full name of people.
    :param kwargs: A dictionary of person names as keys and their age information as values.
                   Each entry in the dictionary should have the person's first name represented
                   as a character (first_name char) and their age as an integer.

    :return: A formatted string list containing the names of all people and their respective ages,
             sorted in ascending order of names.
    """
    list_of_people = ""
    for person in sorted(args):
        if person[:1] in kwargs:
            list_of_people += f"{person} is {kwargs[person[:1]]} years old.\n"

    return list_of_people


def main():
    print(age_assignment("Amy", "Bill", "Willy", W=36,
                         A=22, B=61))


if __name__ == "__main__":
    main()
