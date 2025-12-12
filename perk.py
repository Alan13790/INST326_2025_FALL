def choose_perk(self):
        """
        Author: Alan Z.
        Techniques: Conditional expression
        Prompt the player to select a perk and assign it.
        """
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
        """
        Author: Alan Z.
        Techniques: List comprehension
        Grow all crops and animals. Animal growth increases with perk.
        """
        [crop.grow(1) for crop in self.crops]
        animal_growth = 2 if self.perk == "Animal Breeder" else 1
        [animal.grow(animal_growth) for animal in self.chickens + self.cows]
