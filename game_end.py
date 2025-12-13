def check_game_end(self):
       """Return True if no assets and cannot afford a crop.

       """
       reasons = set()
       if not (self.crops or self.animals):
           reasons.add("no_assets")
       if self.money < CROP_COST:
           reasons.add("cant_afford")
       return reasons == {"no_assets", "cant_afford"}
