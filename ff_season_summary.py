    def season_summary(self):
       """Print achievements.

       """
       print(f"Money: ${self.money}")
       print("Achievements:")
       achieved = [name for name, cond in ACHIEVEMENTS.items() if cond(self.stats)]
       if achieved:
           for name in achieved:
               print(f"- {name}")
       else:
           print("None")
