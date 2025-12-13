def harvest_resources(self):
        """Harvest all mature crops and animals.

        Author: Alan Zheng
        Techniques used:
        - list comprehension
        """
        self.crops = [c for c in self.crops if not self._harvest_item(c, "total_crops_sold")]
        self.animals = [a for a in self.animals if not self._harvest_item(a, "total_animals_sold")]
        self.stats["money"] = self.money

    def player_action(self):
        """Prompt player until a valid action is performed."""
        valid_action = False
        while not valid_action:
            print(
                "Choose an action:\n"
                "  1) Plant a crop\n"
                "  2) Buy a chicken\n"
                "  3) Buy a cow\n"
                "  4) Upgrade farm\n"
                "  5a) Prepare Fields\n"
                "  5b) Check Livestock\n"
                "  5c) Reinforce Farm"
            )
            choice = input("> ").strip().lower()
            actions = {
                "1": self._action_plant_crop,
                "2": self._action_buy_chicken,
                "3": self._action_buy_cow,
                "4": self._action_upgrade_farm,
                "5a": lambda: print("Prepared fields."),
                "5b": lambda: print("Checked livestock."),
                "5c": lambda: print("Reinforced farm."),
                "prepare": lambda: print("Prepared fields."),
                "check": lambda: print("Checked livestock."),
                "reinforce": lambda: print("Reinforced farm.")
            }
            result = actions.get(choice, lambda: print("Invalid choice."))()
            if result is not False:
                valid_action = True
