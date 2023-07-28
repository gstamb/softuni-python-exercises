from task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if task.name == new_task.name:
                return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_tasks = len(self.tasks)
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {all_tasks - len(self.tasks)} tasks."

    def view_section(self):
        return_string_build = ""
        return_string_build += f"Section {self.name}:\n"
        for task in self.tasks:
            return_string_build += f"{task.details()}\n"
        return return_string_build


if __name__ == "__main__":
    pass