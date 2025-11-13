def calculate_final_score(final_money, final_animals, farm_level, scoring_weights=None):
    """
    Author: Sumit Paudel
    Techniques used:
        - f-strings
        - optional parameter (scoring_weights)

    This function figures out the player’s final score at the end of Farm Fortune.
    The score depends on how much money, how many animals, and what farm level
    the player has by the end of the game.
    """

    # use default weights if none are given
    if scoring_weights is None:
        scoring_weights = {"money": 1, "animals": 10, "farm_level": 20}

    # figure out the total score
    score = (
        final_money * scoring_weights["money"]
        + final_animals * scoring_weights["animals"]
        + farm_level * scoring_weights["farm_level"]
    )

    # print a short message based on performance
    if final_money <= 0:
        print("You ran out of money! Better luck next time.")
    elif score < 500:
        print(f"Your score is {score}. You’re a Beginner Farmer!")
    elif score < 1000:
        print(f"Your score is {score}. You’re a Skilled Farmer!")
    elif score < 2000:
        print(f"Your score is {score}. You’re an Expert Farmer!")
    else:
        print(f"Your score is {score}. You’re a Legendary Farmer!")

    return score
