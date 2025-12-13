def handle_events(self):
    """
    Handles random farm events with probabilities affected by perks.

    Author: Andrew Cusi
    Techniques used:
    Set operations (union)
    Conditonal Epxressions
    """
    multiplier = 0.8 if self.perk == "Risk Manager" else 1.0
    candidates = {'crop'} if self.crops else set()
    candidates |= {'animal'} if self.animals else set()
    if not candidates:
        return
    if random.random() < 0.3 * multiplier:
        self._event_golden(random.choice(list(candidates)))
    if random.random() < 0.3 * multiplier:
        self._event_slow(random.choice(list(candidates)))
    if random.random() < 0.2 * multiplier:
        self._event_disaster(random.choice(list(candidates)))


def _event_golden(self, target):
    """
    Handles the 'golden' event for crops or animals.

    """
    if target == 'crop' and self.crops:
        bonus = 15 if self.perk == "Crop Specialist" else 0
        for c in self.crops:
            c.sell_price = 75 + bonus
        print("EVENT: Golden Season! Crops will sell higher.")
    elif target == 'animal' and self.animals:
        for a in self.animals:
            a.grow(1)
        print("EVENT: Vaccination! Animals grow faster.")


def _event_slow(self, target):
    """
    Handles the 'slow' event for crops or animals.

    """
    if target == 'crop' and self.crops:
        for c in self.crops:
            c.growth_time += 2
            c.sell_price = 35
        print("EVENT: Pest Infestation! Crops slowed.")
    elif target == 'animal' and self.animals:
        for a in self.animals:
            a.growth_time += 1
        print("EVENT: Animal Illness! Animals take longer to grow.")


def _event_disaster(self, target):
    """
    Handles the 'disaster' event for crops or animals.
    
    """
    if target == 'crop' and self.crops:
        self.crops = []
        print("EVENT: Drought! All crops destroyed.")
    elif target == 'animal' and self.animals:
        self.animals = []
        print("EVENT: Rabies Outbreak! All animals died.")

