### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

# === Class ===

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


# === Main Program ===

def print_report(machine):
    print(f"Bread: {machine.machine_resources['bread']} slice(s)")
    print(f"Ham: {machine.machine_resources['ham']} slice(s)")
    print(f"Cheese: {machine.machine_resources['cheese']} pound(s)")


def main():
    machine = SandwichMachine(resources)

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            print_report(machine)
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if machine.check_resources(ingredients):
                coins = machine.process_coins()
                if machine.transaction_result(coins, cost):
                    machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid input. Please choose again.")


if __name__ == "__main__":
    main()