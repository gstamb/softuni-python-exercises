class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget = budget

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, animal_capacity):
        self.__animal_capacity = animal_capacity

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, workers_capacity):
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price: int):
        if self.budget >= price and self.animal_capacity > 0:
            self.animals.append(animal)
            self.budget -= price
            self.animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.animal_capacity > 1 and self.budget < price:
            return f"Not enough budget"
        elif self.budget >= price and self.animal_capacity <= len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker):
        for employee in self.workers:
            if employee.name == worker:
                self.workers.remove(employee)
                return f"{worker} fired successfully"
        else:
            return f"There is no {worker} in the zoo"

    def pay_workers(self):
        salary_total = 0
        for worker in self.workers:
            salary_total += worker.salary
        if self.budget - salary_total >= 0:
            self.budget -= salary_total
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_upkeep = 0
        for animal in self.animals:
            animal_upkeep += animal.money_for_care
        if self.budget >= animal_upkeep:
            self.budget -= animal_upkeep
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        animal_status_info = f"You have {len(self.animals)} animals\n"
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        cheetah = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        if lions:
            animal_status_info += f"----- {len(lions)} Lions:\n"
            for lion in lions:
                animal_status_info += f"{lion.__repr__()}\n"
        if tigers:
            animal_status_info += f"----- {len(tigers)} Tigers:\n"
            for tiger in tigers:
                animal_status_info += f"{tiger.__repr__()}\n"
        if cheetah:
            animal_status_info += f"----- {len(cheetah)} Cheetahs:\n"
            for kitty in cheetah:
                animal_status_info += f"{kitty.__repr__()}\n"

        return animal_status_info.strip()

    def workers_status(self):
        worker_status_info = f"You have {len(self.workers)} workers\n"
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        if keepers:
            worker_status_info += f"----- {len(keepers)} Keepers:\n"
            for keeper in keepers:
                worker_status_info += f"{keeper.__repr__()}\n"
        if caretakers:
            worker_status_info += f"----- {len(caretakers)} Caretakers:\n"
            for caretaker in caretakers:
                worker_status_info += f"{caretaker.__repr__()}\n"
        if vets:
            worker_status_info += f"----- {len(vets)} Vets:\n"
            for vet in vets:
                worker_status_info += f"{vet.__repr__()}\n"

        return worker_status_info.strip()
