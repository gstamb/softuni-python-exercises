class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        combined_members = self.people + other.people
        return Group(f"{self.name} {other.name}", combined_members)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(x) for x in self.people])}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"
