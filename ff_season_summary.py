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
