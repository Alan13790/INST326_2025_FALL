class Farm:
    def __init__(self):
        """
        Initialize farm state including money, slots, animals, crops, and stats.
        """
        self.money = STARTING_MONEY
        self.season = 1
        self.level = 0
        self.crop_slots = BASE_CROP_SLOTS
        self.animal_slots = BASE_ANIMAL_SLOTS

        self.crops = []
        self.chickens = []
        self.cows = []

        self.temp_crop_protection = 0
        self.temp_animal_protection = 0
        self.temp_disaster_protection = 0

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
        """
        Return the number of free crop slots.
        """
        return max(self.crop_slots - len(self.crops), 0)

    def available_animal_slots(self):
        """
        Return the number of free animal slots.
        """
        return max(self.animal_slots - len(self.chickens) - len(self.cows), 0)
