class Resource:
    """
    Base class for crops and animals.
    """
    def __init__(self, growth_time, sell_price, name):
        self.growth_done = 0
        self.growth_time = growth_time
        self.sell_price = sell_price
        self.name = name

    def grow(self, amount=1):
        """Increase growth progress.
        
        """
        if amount > 0:
            self.growth_done += amount

    def is_mature(self):
        """Return True if fully grown.

        """
        return self.growth_done >= self.growth_time

    def status(self):
        """Return a string describing remaining growth and sell price.

        """
        remaining = max(self.growth_time - self.growth_done, 0)
        return f"{self.name}: {remaining} seasons until mature — sell ${self.sell_price}"

    def __len__(self):
        """Number of seasons left to mature.
        
        """
        return max(self.growth_time - self.growth_done, 0)

    def __str__(self):
        """Return string representation of resource.
        
        """
        return f"{self.name} ({self.growth_done}/{self.growth_time})"

class Crop(Resource):
    """
    Crop resource class.

    Author: Alan Zheng
    Technique Used: Optional Parameters
    """
    def __init__(self, sell_price=None, growth_time=None):
        sp = CROP_BASE_SELL if sell_price is None else sell_price
        gt = CROP_GROWTH if growth_time is None else growth_time
        super().__init__(gt, sp, "Crop")

    def __repr__(self):
        return f"<Crop {self.growth_done}/{self.growth_time} sell={self.sell_price}>"

class Animal(Resource):
    """
    Animal resource class.
    """
    def __init__(self, species, sell_price, growth_time):
        super().__init__(growth_time, sell_price, species)

    def __repr__(self):
        return f"<Animal {self.name} {self.growth_done}/{self.growth_time} sell={self.sell_price}>"
