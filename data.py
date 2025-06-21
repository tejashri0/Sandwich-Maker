# This file holds all the data used in the sandwich maker.
# Think of it like the machine’s built-in recipe book and inventory tracker.

# Recipes for different sandwich sizes
recipes = {
    "small": {
        "ingredients": {"bread": 2, "ham": 4, "cheese": 4},
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {"bread": 4, "ham": 6, "cheese": 8},
        "cost": 3.25,
    },
    "large": {
        "ingredients": {"bread": 6, "ham": 8, "cheese": 12},
        "cost": 5.5,
    }
}

# Starting amount of ingredients available in the machine
resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}