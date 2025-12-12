    def available_crop_slots(self):
    """Return the number of empty crop slots available."""
        return max(self.crop_slots - len(self.crops), 0)

    def available_animal_slots(self):
    """Return the number of empty animal slots available."""
        return max(self.animal_slots - len(self.chickens) - len(self.cows), 0)

    def choose_perk(self):
    """Let the player select a perk that affects growth, sales, or events."""
        print("Choose a perk:")
        print("1) Crop Specialist → crops sell +$15")
        print("2) Animal Breeder → animals grow 1 season earlier but sell for 15% less")
        print("3) Risk Manager → -20% chance of negative events.")
        choice = input("> ")
        self.perk = ("Crop Specialist" if choice == "1"
                     else "Animal Breeder" if choice == "2"
                     else "Risk Manager" if choice == "3"
                     else None)

    def grow_resources(self):
    """Advance growth for all crops and animals, modified by perks."""
        [crop.grow(1) for crop in self.crops]
        animal_growth = 2 if self.perk == "Animal Breeder" else 1
        [animal.grow(animal_growth) for animal in self.chickens + self.cows]
