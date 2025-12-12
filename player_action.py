def player_action(self):
    """
    Prompt the player to choose an action for the season.

    Actions:
        1) Plant a crop: Spend money to plant if slots and funds allow.
        2) Buy a chicken: Purchase a chicken with growth and sell price affected by perks.
        3) Buy a cow: Purchase a cow with growth and sell price affected by perks.
        4) Upgrade farm: Increase farm level, slots, and optionally choose a perk.
        5) Seasonal action: Perform one-time actions to reduce crop, animal, or disaster risks.

    Handles invalid inputs by notifying the player.
    Updates money, farm stats, and temporary protections accordingly.
    """
  
        print(
            "Choose an action:\n"
            "  1) Plant a crop\n"
            "  2) Buy a chicken\n"
            "  3) Buy a cow\n"
            "  4) Upgrade farm\n"
            "  5) Seasonal action"
        )
        choice = input("> ").strip().lower()
        if choice == "1":
            if self.money >= CROP_COST and self.available_crop_slots() > 0:
                sell_price = CROP_BASE_SELL + (15 if self.perk == "Crop Specialist" else 0)
                self.crops.append(Crop(sell_price))
                self.money -= CROP_COST
                self.stats['total_crops_grown'] += 1
                print("You planted a crop.")
            else:
                print("Cannot plant a crop.")
        elif choice == "2":
            if self.money >= CHICKEN_COST and self.available_animal_slots() > 0:
                base_price = CHICKEN_SELL
                growth = CHICKEN_GROWTH
                if self.perk == "Animal Breeder":
                    base_price = int(base_price * 0.85)
                    growth -= 1
                self.chickens.append(Animal("Chicken", base_price, growth))
                self.money -= CHICKEN_COST
                self.stats['total_chickens_born'] += 1
                print("You bought a chicken.")
            else:
                print("Cannot buy a chicken.")
        elif choice == "3":
            if self.money >= COW_COST and self.available_animal_slots() > 0:
                base_price = COW_SELL
                growth = COW_GROWTH
                if self.perk == "Animal Breeder":
                    base_price = int(base_price * 0.85)
                    growth -= 1
                self.cows.append(Animal("Cow", base_price, growth))
                self.money -= COW_COST
                self.stats['total_cows_born'] += 1
                print("You bought a cow.")
            else:
                print("Cannot buy a cow.")
        elif choice == "4":
            if self.money >= FARM_UPGRADE_COST:
                self.money -= FARM_UPGRADE_COST
                self.level += 1
                self.crop_slots += 2
                self.animal_slots += 1
                print(f"Farm upgraded to level {self.level}")
                self.choose_perk()
            else:
                print("Not enough money to upgrade.")
        elif choice == "5":
            while True:
                print(
                    "Seasonal actions:\n"
                    "  a) Prepare Fields (reduce crop bad-event chance by 10%)\n"
                    "  b) Check Livestock (reduce animal bad-event chance by 10%)\n"
                    "  c) Reinforce Farm (reduce all disasters by 5%)"
                )
                seasonal_choice = input("> ").strip().lower()
                if seasonal_choice in ["a", "prepare"]:
                    self.temp_crop_protection += 0.1
                    print("Prepared fields.")
                    break
                elif seasonal_choice in ["b", "check"]:
                    self.temp_animal_protection += 0.1
                    print("Checked animals.")
                    break
                elif seasonal_choice in ["c", "reinforce"]:
                    self.temp_disaster_protection += 0.05
                    print("Reinforced farm.")
                    break
                else:
                    print("Invalid seasonal action choice. Please choose a, b, or c.")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
