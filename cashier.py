# This file handles all money-related tasks.
# The Cashier class collects money and checks if the transaction is successful.

class Cashier:
    def process_coins(self):
        # Ask user to insert coins and calculate the total value
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return round(total, 2)

    def transaction_result(self, coins, cost):
        # Determine if the inserted coins are enough and provide change if needed
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
        return True
