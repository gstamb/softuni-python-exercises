from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

        self.customer_lookup = {}
        self.trainer_lookup = {}
        self.equipment_lookup = {}
        self.plan_lookup = {}
        self.subscription_lookup = {}

    def add_customer(self, customer: Customer):
        if customer.id not in self.customer_lookup:
            self.customer_lookup[customer.id] = len(self.customers)
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer.id not in self.trainer_lookup:
            self.trainer_lookup[trainer.id] = len(self.trainers)
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment.id not in self.equipment_lookup:
            self.equipment_lookup[equipment.id] = len(self.equipment)
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan.id not in self.plan_lookup:
            self.plan_lookup[plan.id] = len(self.plans)
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription.id not in self.subscription_lookup:
            self.subscription_lookup[subscription.id] = len(self.subscriptions)
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result_str = ""
        if self.subscriptions:
            result_str += ", ".join([str(x) for x in self.subscriptions]) + "\n"
        if self.customers:
            result_str += ", ".join([str(x) for x in self.customers]) + "\n"
        if self.trainers:
            result_str += ", ".join([str(x) for x in self.trainers]) + "\n"

        if self.equipment:
            result_str += ", ".join([str(x) for x in self.equipment]) + "\n"

        if self.plans:
            result_str += ", ".join([str(x) for x in self.plans])

        return result_str
