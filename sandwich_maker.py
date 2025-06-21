# This file contains the SandwichMaker class.
# It manages sandwich-making and tracks ingredients.

class SandwichMaker:
    def __init__(self, machine_resources):
        # Save the available ingredients when the machine starts
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        # Check if there are enough ingredients to make the chosen sandwich
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        # Deduct the used ingredients and prepare the sandwich
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def print_report(self):
        # Print the current amount of each ingredient available
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")
