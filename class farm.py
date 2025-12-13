class Farm:
    """
    Main farm class. Manages resources, money, perks, stats, and seasons.
    """
    def __init__(self):
        self.money = STARTING_MONEY
        self.season = 1
        self.level = 0
        self.crop_slots = BASE_CROP_SLOTS
        self.animal_slots = BASE_ANIMAL_SLOTS
        self.crops = []
        self.animals = []
        self.perk = None
        self.stats = {
            'total_crops_grown': 0,
            'total_chickens_born': 0,
            'total_cows_born': 0,
            'total_crops_sold': 0,
            'total_chickens_sold': 0,
            'total_cows_sold': 0,
            'money': self.money
        }

    def available_crop_slots(self):
        """Return number of empty crop slots.

        Auhtor: Alan Zheng
        Techniques used:
        - comprehensions or generator expressions
        """
        used = sum(1 for _ in self.crops)
        return self.crop_slots - used if used < self.crop_slots else 0

    def available_animal_slots(self):
        """Return number of empty animal slots.

        """
        used = 0
        idx = 0
        while idx < len(self.animals):
            used += 1
            idx += 1
        return max(self.animal_slots - used, 0)
