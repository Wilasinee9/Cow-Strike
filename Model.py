import random

class CowModel:
    def __init__(self, cow_id, age_years, age_months, udders):
        self.cow_id = cow_id
        self.age_years = age_years
        self.age_months = age_months
        self.udders = udders

    def milk(self):
        if self.udders == 4:
            if random.random() < 0.05:
                self.udders -= 1  # Reduce udders by 1 with 5% chance
            return self.age_years + self.age_months / 12
        return 0

    def restore_udders(self):
        if self.udders == 3 and random.random() < 0.20:
            self.udders = 4

class GoatModel:
    def __init__(self, goat_id):
        self.goat_id = goat_id
