def _action_plant_crop(self):
    """
    Plants a crop if money and crop slots are available.

    Author: Sumit Paudel
    Techniques used:
    - Conditional expressions for perk bonus
    - f-strings for dynamic messages
    """
    if self.money < CROP_COST:
        print(f"Not enough money to plant a crop (Need ${CROP_COST}). Choose something else.")
        return False
    if self.available_crop_slots() <= 0:
        print("No crop slots available. Choose something else.")
        return False
    bonus = 15 if self.perk == "Crop Specialist" else 0
    self.crops.append(Crop(sell_price=CROP_BASE_SELL + bonus))
    self.money -= CROP_COST
    self.stats["total_crops_grown"] += 1
    print("You planted a crop.")


def _action_buy_chicken(self):
    """
    Purchases a chicken if money and animal slots are available.

    """
    if self.money < CHICKEN_COST:
        print(f"Not enough money to buy a chicken (Need ${CHICKEN_COST}). Choose something else.")
        return False
    if self.available_animal_slots() <= 0:
        print("No animal slots available. Choose something else.")
        return False
    price = int(CHICKEN_SELL * 0.85) if self.perk == "Animal Breeder" else CHICKEN_SELL
    growth = CHICKEN_GROWTH - 1 if self.perk == "Animal Breeder" else CHICKEN_GROWTH
    self.animals.append(Animal("Chicken", price, growth))
    self.money -= CHICKEN_COST
    self.stats["total_chickens_born"] += 1
    print("You bought a chicken.")


def _action_buy_cow(self):
    """
    Purchases a cow if money and animal slots are available.

    Author: Sumit Paudel
    Techniques used:
    - sequence unpacking 
    """
    if self.money < COW_COST:
        print(f"Not enough money to buy a cow (Need ${COW_COST}). Choose something else.")
        return False
    if self.available_animal_slots() <= 0:
        print("No animal slots available. Choose something else.")
        return False
    price, growth = (int(COW_SELL * 0.85), COW_GROWTH - 1) if self.perk == "Animal Breeder" else (COW_SELL, COW_GROWTH)
    self.animals.append(Animal("Cow", price, growth))
    self.money -= COW_COST
    self.stats["total_cows_born"] += 1
    print("You bought a cow.")


def _action_upgrade_farm(self):
    """
    Upgrades the farm if enough money is available.

    """
    if self.money < FARM_UPGRADE_COST:
        print(f"Not enough money to upgrade the farm (Need ${FARM_UPGRADE_COST}). Choose something else.")
        return False
    self.money -= FARM_UPGRADE_COST
    self.level += 1
    self.crop_slots += 2
    self.animal_slots += 1
    print(f"Farm upgraded to level {self.level}!")
    self.choose_perk()
