## This is the entry point of the Sandwich Maker Machine program.
# It brings everything together: data, sandwich maker, and cashier.

import data  # importing recipes and resources
import sandwich_maker  # importing sandwich logic
import cashier  # importing cashier logic

def main():
    # Load recipes and ingredient stock from data module
    resources = data.resources
    recipes = data.recipes

    # Create objects from each class to use their functions
    maker = sandwich_maker.SandwichMaker(resources)
    cashier_obj = cashier.Cashier()

    # Program runs in a loop until user types 'off'
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break  # stop the machine
        elif choice == "report":
            maker.print_report()  # show current ingredients
        elif choice in recipes:
            # If valid sandwich is chosen, proceed step-by-step
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if maker.check_resources(ingredients):
                coins = cashier_obj.process_coins()
                if cashier_obj.transaction_result(coins, cost):
                    maker.make_sandwich(choice, ingredients)
        else:
            print("Invalid input. Please choose again.")

if __name__ == "__main__":
    main()
