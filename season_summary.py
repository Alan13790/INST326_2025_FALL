    def season_summary(self):
       """Print achievements.


       Techniques used:
       - comprehensions / generator expressions
       - f-strings containing expressions
       """
       print(f"Money: ${self.money}")
       print("Achievements:")
       achieved = [name for name, cond in ACHIEVEMENTS.items() if cond(self.stats)]
       if achieved:
           for name in achieved:
               print(f"- {name}")
       else:
           print("None")


   def check_game_end(self):
       """Return True if no assets and cannot afford a crop.


       Techniques used:
       - set operations (union)
       """
       reasons = set()
       if not (self.crops or self.animals):
           reasons.add("no_assets")
       if self.money < CROP_COST:
           reasons.add("cant_afford")
       return reasons == {"no_assets", "cant_afford"}


   def final_score(self):
       """Calculate and print final score.


       Techniques used:
       - f-strings containing expressions
       """
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