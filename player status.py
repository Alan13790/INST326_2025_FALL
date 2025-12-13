def print_status(self):
        """Print the current season status.
        
        """
        print(f"\nSeason {self.season} of {MAX_SEASONS}")
        print(f"Money: ${self.money} | Farm Level: {self.level}")
        print(f"Crops: {len(self.crops)}/{self.crop_slots} | Animals: {len(self.animals)}/{self.animal_slots}")

        print("Crops status:")
        for i, crop in enumerate(sorted(self.crops, key=lambda c: c.growth_done)):
            print(f"{i+1}) {crop.status()}")

        print("Animals status:")
        for i, animal in enumerate(sorted(self.animals, key=lambda a: a.sell_price, reverse=True)):
            print(f"{i+1}) {animal.status()}")
