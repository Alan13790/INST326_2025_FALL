"""
Farm simulation

This module defines all constants used in the farm simulation game,
including economic values, growth rates, slot limits, and
achievement conditions. It also stores achievement rules
"""

import random


"""Maximum number of seasons the game can run."""
MAX_SEASONS = 24

"""Amount of money the player starts with."""
STARTING_MONEY = 100


"""Cost to plant a single crop."""
CROP_COST = 25

"""Base selling price for a harvested crop."""
CROP_BASE_SELL = 50

"""Number of seasons required for crops to grow."""
CROP_GROWTH = 2


"""Cost to purchase a chicken."""
CHICKEN_COST = 75

"""Selling price of a chicken."""
CHICKEN_SELL = 150

"""Number of seasons required for chickens to reproduce."""
CHICKEN_GROWTH = 3


"""Cost to purchase a cow."""
COW_COST = 150

"""Selling price of a cow."""
COW_SELL = 350

"""Number of seasons required for cows to reproduce."""
COW_GROWTH = 4


"""Cost to upgrade the farm, increasing available slots."""
FARM_UPGRADE_COST = 500


"""Initial number of crop slots available on the farm."""
BASE_CROP_SLOTS = 3

"""Initial number of animal slots available on the farm."""
BASE_ANIMAL_SLOTS = 2


"""
Dictionary mapping achievement names to lambda functions.

Each lambda takes a game state dictionary `s` and returns True
if the achievement condition has been met.
"""
ACHIEVEMENTS = {
   "Prosperous": lambda s: s['money'] >= 2000,
   "Herder": lambda s: s['total_cows_born'] >= 5 and s['total_chickens_born'] >= 10,
   "Master Cultivator": lambda s: s['total_crops_grown'] >= 20
}
