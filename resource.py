class Resource:
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
        """
        Author: Alan Z.
        Techniques: f-strings with expressions
        Return a formatted string showing growth status and sell price.
        """
        done = min(self.growth_done, self.growth_time)
        return f"{self.name}: {done}/{self.growth_time} grown — sell ${self.sell_price}"


class Crop(Resource):
    def __init__(self, sell_price=None, growth_time=None):
        """
        Author: Andrew C.
        Techniques: Optional parameters
        Initialize a crop with optional sell price and growth time.
        """
        if sell_price is None:
            sell_price = CROP_BASE_SELL
        if growth_time is None:
            growth_time = CROP_GROWTH
        super().__init__(growth_time, sell_price, "Crop")


class Animal(Resource):
    def __init__(self, species, sell_price, growth_time):
        super().__init__(growth_time, sell_price, species)
