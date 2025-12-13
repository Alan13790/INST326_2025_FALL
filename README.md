Running the program: This program does not take command-line arguments.
All inputs are handled interactively during the game.
You need Python 3 installed on your system.

How to play/output: crops & animals automatically sell when mature

Press 5a,5b,5c instead of just 5 then the letter

5a:Prepare Fields → reduce chance of crop bad event this season by %10
5b:Check Livestock → reduce chance of animal bad event by %10
5c:Reinforce Farm → reduce chance of disasters by a 5%

Achievements are automatically checked each season
Achievement	Condition:
Prosperous	Money ≥ $2000
Herder	≥5 cows born and ≥10 chickens born
Master Cultivator	≥20 crops grown

The game ends if:
You have no crops or animals, AND
You cannot afford a crop (money < 25)
Otherwise, the game ends automatically after 24 seasons.

Attribution:
| Method / Function       | Primary Author   | Techniques Demonstrated              |
|------------------------|----------------|------------------------------------------|
| available_crop_slots    | Alan Zheng      | Comprehension or generator expression |
| __init__                | Alan Zheng      | Optional Parameter                    |
| harvest_resources       | Alan Zheng      | List Comprehension                    |
| handle_events           | Andrew Cusi     | Conditional expression                |  
| handle_events           | Andrew Cusi     | Set Operations                        |
| _action_buy_cow         | Sumit Paudel    | Sequence Unpacking                    |
| _action_plant_crop      | Sumit Paudel    | f-strings                             |
| print_status            | Sumit Paudel    | Lambda                                |


