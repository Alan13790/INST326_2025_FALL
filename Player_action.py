    def player_action(self):
        """
        Author: Alan Z.
        Techniques: Conditional expressions, f-strings
        Allow player to choose an action and apply its effects.
        """
        print(
            "Choose an action:\n"
            "  1) Plant a crop\n"
            "  2) Buy a chicken\n"
            "  3) Buy a cow\n"
            "  4) Upgrade farm\n"
            "  5) Seasonal action\n"
            "       - Prepare Fields (reduce crop bad-event chance by 10% this season)\n"
            "       - Check Livestock (reduce animal bad-event chance by 10% this season)\n"
            "       - Reinforce Farm (reduce all disasters by 5% this season)"
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
                if self.perk == "Animal Breeder":
                    base_price = int(base_price * 0.85)
                    growth = CHICKEN_GROWTH - 1
                else:
                    growth = CHICKEN_GROWTH
                self.chickens.append(Animal("Chicken", base_price, growth))
                self.money -= CHICKEN_COST
                self.stats['total_chickens_born'] += 1
                print("You bought a chicken.")
            else:
                print("Cannot buy a chicken.")
        elif choice == "3":
            if self.money >= COW_COST and self.available_animal_slots() > 0:
                base_price = COW_SELL
                if self.perk == "Animal Breeder":
                    base_price = int(base_price * 0.85)
                    growth = COW_GROWTH - 1
                else:
                    growth = COW_GROWTH
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
        elif choice.startswith("5") or choice in ["a", "b", "c"]:
            if choice in ["a", "prepare"]:
                self.temp_crop_protection += 0.1
                print("Prepared fields.")
            elif choice in ["b", "check"]:
                self.temp_animal_protection += 0.1
                print("Checked animals.")
            elif choice in ["c", "reinforce"]:
                self.temp_disaster_protection += 0.05
                print("Reinforced farm.")
        else:
            print("Invalid choice.")
