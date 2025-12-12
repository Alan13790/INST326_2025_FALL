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
