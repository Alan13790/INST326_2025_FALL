class Farm:
    """
    The player's farm, tracking money, season, slots, resources, perks, and stats.

    Attributes:
        money (int): Farm money.
        season (int): Current season.
        crops, chickens, cows (list): Farm resources.
        crop_slots, animal_slots (int): Maximum allowed resources.
        temp_crop_protection, temp_animal_protection, temp_disaster_protection (int): Temporary defenses.
        perk (str or None): Current perk.
        stats (dict): Tracks growth, sales, and money.
    """

    def __init__(self):
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
