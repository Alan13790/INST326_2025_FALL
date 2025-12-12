class Resource:
    """
    A generic farm resource (crop or animal).
    Attributes:
        growth_done (int): Current growth progress.
        growth_time (int): Growth required to mature.
        sell_price (int): Value when sold.
        name (str): Resource name.

    Methods:
        grow(amount=1): Increases growth.
        is_mature(): Returns True if fully grown.
        status(): Returns growth and sell price info.
    """

    def __init__(self, growth_time, sell_price, name):
        self.growth_done = 0
        self.growth_time = growth_time
        self.time_to_grow = growth_time
        self.sell_price = sell_price
        self.name = name

    def grow(self, amount=1):
        self.growth_done += amount

    def is_mature(self):
        return True if self.growth_done >= self.growth_time else False

    def status(self):
        done = min(self.growth_done, self.growth_time)
        return f"{self.name}: {done}/{self.growth_time} grown — sell ${self.sell_price}"

class Crop(Resource):
    def __init__(self, sell_price=None, growth_time=None):
        if sell_price is None:
            sell_price = CROP_BASE_SELL
        if growth_time is None:
            growth_time = CROP_GROWTH
        super().__init__(growth_time, sell_price, "Crop")

class Animal(Resource):
    def __init__(self, species, sell_price, growth_time):
        super().__init__(growth_time, sell_price, species)

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
