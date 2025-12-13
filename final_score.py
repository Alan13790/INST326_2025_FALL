def final_score(self):
       """Calculate and print final score.

       """
       remaining = sum(r.sell_price for r in self.crops + self.animals)
       score = self.money + remaining + self.level * 100
       print(f"Final Money: ${self.money}")
       print(f"Farm Level: {self.level}")
       print(f"Final Score: {score}")
