import random

MAX_SEASONS = 24
STARTING_MONEY = 100

CROP_COST = 25
CROP_BASE_SELL = 50
CROP_GROWTH = 2

CHICKEN_COST = 75
CHICKEN_SELL = 150
CHICKEN_GROWTH = 3

COW_COST = 150
COW_SELL = 350
COW_GROWTH = 4

FARM_UPGRADE_COST = 500

BASE_CROP_SLOTS = 3
BASE_ANIMAL_SLOTS = 2

ACHIEVEMENTS = {
    "Prosperous": lambda s: s['money'] >= 2000,
    "Herder": lambda s: s['total_cows_born'] >= 5 and s['total_chickens_born'] >= 10,
    "Master Cultivator": lambda s: s['total_crops_grown'] >= 20
}


class Resource:
    def __init__(self, growth_time, sell_price, name):
        self.growth_done = 0
        self.growth_time = growth_time
        self.sell_price = sell_price
        self.name = name

    def grow(self, amount=1):
        if amount > 0:
            self.growth_done += amount

    def is_mature(self):
        return self.growth_done >= self.growth_time

    def status(self):
        remaining = max(self.growth_time - self.growth_done, 0)
        return f"{self.name}: {remaining} seasons until mature — sell ${self.sell_price}"

    def __len__(self):
        return max(self.growth_time - self.growth_done, 0)

    def __str__(self):
        return f"{self.name} ({self.growth_done}/{self.growth_time})"


class Crop(Resource):
    def __init__(self, sell_price=None, growth_time=None):
        sp = CROP_BASE_SELL if sell_price is None else sell_price
        gt = CROP_GROWTH if growth_time is None else growth_time
        super().__init__(gt, sp, "Crop")

    def __repr__(self):
        return f"<Crop {self.growth_done}/{self.growth_time} sell={self.sell_price}>"


class Animal(Resource):
    def __init__(self, species, sell_price, growth_time):
        super().__init__(growth_time, sell_price, species)

    def __repr__(self):
        return f"<Animal {self.name} {self.growth_done}/{self.growth_time} sell={self.sell_price}>"


class Farm:
    def __init__(self):
        self.money = STARTING_MONEY
        self.season = 1
        self.level = 0
        self.crop_slots = BASE_CROP_SLOTS
        self.animal_slots = BASE_ANIMAL_SLOTS
        self.crops = []
        self.animals = []
        self.perk = None
        self.stats = {
            'total_crops_grown': 0,
            'total_chickens_born': 0,
            'total_cows_born': 0,
            'total_crops_sold': 0,
            'total_chickens_sold': 0,
            'total_cows_sold': 0,
            'money': self.money
        }

    def available_crop_slots(self):
        used = sum(1 for _ in self.crops)
        return self.crop_slots - used if used < self.crop_slots else 0

    def available_animal_slots(self):
        used = 0
        idx = 0
        while idx < len(self.animals):
            used += 1
            idx += 1
        return max(self.animal_slots - used, 0)

    def choose_perk(self):
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
        for crop in self.crops:
            crop.grow(1)
        growth = 2 if self.perk == "Animal Breeder" else 1
        idx = 0
        while idx < len(self.animals):
            self.animals[idx].grow(growth)
            idx += 1

    def handle_events(self):
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
        if target == 'crop' and self.crops:
            self.crops = []
            print("EVENT: Drought! All crops destroyed.")
        elif target == 'animal' and self.animals:
            self.animals = []
            print("EVENT: Rabies Outbreak! All animals died.")

    def _harvest_item(self, item, stat_key):
        if item.is_mature():
            self.money += item.sell_price
            self.stats[stat_key] += 1
            return True
        return False

    def harvest_resources(self):
        self.crops = [c for c in self.crops if not self._harvest_item(c, "total_crops_sold")]
        self.animals = [a for a in self.animals if not self._harvest_item(a, "total_animals_sold")]
        self.stats["money"] = self.money

    def player_action(self):
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

    def _action_plant_crop(self):
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
        if self.money < FARM_UPGRADE_COST:
            print(f"Not enough money to upgrade the farm (Need ${FARM_UPGRADE_COST}). Choose something else.")
            return False
        self.money -= FARM_UPGRADE_COST
        self.level += 1
        self.crop_slots += 2
        self.animal_slots += 1
        print(f"Farm upgraded to level {self.level}!")
        self.choose_perk()

    def print_status(self):
        print(f"\nSeason {self.season} of {MAX_SEASONS}")
        print(f"Money: ${self.money} | Farm Level: {self.level}")
        print(f"Crops: {len(self.crops)}/{self.crop_slots} | Animals: {len(self.animals)}/{self.animal_slots}")

        print("Crops status:")
        for i, crop in enumerate(sorted(self.crops, key=lambda c: c.growth_done)):
            print(f"{i+1}) {crop.status()}")

        print("Animals status:")
        for i, animal in enumerate(sorted(self.animals, key=lambda a: a.sell_price, reverse=True)):
            print(f"{i+1}) {animal.status()}")

    def season_summary(self):
        print(f"Money: ${self.money}")
        print("Achievements:")
        achieved = [name for name, cond in ACHIEVEMENTS.items() if cond(self.stats)]
        if achieved:
            for name in achieved:
                print(f"- {name}")
        else:
            print("None")

    def check_game_end(self):
        reasons = set()
        if not (self.crops or self.animals):
            reasons.add("no_assets")
        if self.money < CROP_COST:
            reasons.add("cant_afford")
        return reasons == {"no_assets", "cant_afford"}

    def final_score(self):
        remaining = sum(r.sell_price for r in self.crops + self.animals)
        score = self.money + remaining + self.level * 100
        print(f"Final Money: ${self.money}")
        print(f"Farm Level: {self.level}")
        print(f"Final Score: {score}")


def main():
    farm = Farm()
    print("Welcome to Farm Fortune!")
    farm.choose_perk()

    while farm.season <= MAX_SEASONS:
        farm.print_status()
        farm.grow_resources()
        farm.handle_events()
        farm.player_action()
        farm.harvest_resources()
        farm.season_summary()

        if farm.check_game_end():
            print("GAME OVER: You have no money and nothing growing.")
            break

        farm.season += 1

    farm.final_score()


if __name__ == "__main__":
    main()
