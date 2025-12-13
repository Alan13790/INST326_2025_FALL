def choose_perk(self):
    """
    Prompts the player to select a gameplay perk.

    Displays available perk options, reads user input, and assigns
    the selected perk to the player. If the input is invalid, no perk
    is assigned and a message is displayed.
    """
    print("Choose a perk:")
    print("1) Crop Specialist → crops sell +$15")
    print("2) Animal Breeder → animals grow 1 season earlier but sell 15% less")
    print("3) Risk Manager → -20% chance of negative events")
    choice = input("> ").strip()
    self.perk = (
        "Crop Specialist" if choice == "1"
        else "Animal Breeder" if choice == "2"
        else "Risk Manager" if choice == "3"
        else None
    )
    if self.perk is None:
        print("No valid perk chosen.")


def grow_resources(self):
    """
    Advances growth for all crops and animals on the farm.

    Crops always grow by one season. Animals grow by one season,
    or by two seasons if the player has the Animal Breeder perk.
    """
    for crop in self.crops:
        crop.grow(1)
    growth = 2 if self.perk == "Animal Breeder" else 1
    idx = 0
    while idx < len(self.animals):
        self.animals[idx].grow(growth)
        idx += 1
