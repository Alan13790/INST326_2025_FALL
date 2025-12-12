import random

MAX_SEASONS = 24
STARTING_MONEY = 100

CROP_COST = 25
CROP_BASE_SELL = 50
CROP_GROWTH = 2

CHICKEN_COST = 75
CHICKEN_SELL = 150
CHICKEN_GROWTH = 3

COW_COST = 150
COW_SELL = 350
COW_GROWTH = 4

FARM_UPGRADE_COST = 500

BASE_CROP_SLOTS = 3
BASE_ANIMAL_SLOTS = 2

ACHIEVEMENTS = {
    "Prosperous": lambda s: s['money'] >= 2000,
    "Herder": lambda s: s['total_cows_born'] >= 5 and s['total_chickens_born'] >= 10,
    "Master Cultivator": lambda s: s['total_crops_grown'] >= 20
}
"""
Author: Andrew C.
Techniques: Lambda Function
"""
