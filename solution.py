class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money

    def get_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Money: ${self.money:.2f}")

    def turn_off(self):
        print("Turning off the coffee machine.")
        exit()

    def check_resources(self, water_needed, milk_needed, beans_needed):
        return self.water >= water_needed and self.milk >= milk_needed and self.coffee_beans >= beans_needed

    def make_coffee(self, coffee_type, cost, water_needed, milk_needed, beans_needed):
        if self.check_resources(water_needed, milk_needed, beans_needed):
            print(f"Making {coffee_type}...")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.money += cost
            print(f"Here is your {coffee_type}. Enjoy!")
        else:
            print(f"Sorry, not enough resources to make {coffee_type}.")

    def insert_coins(self):
        print("Please insert coins.")
       
        euros = int(input("How many euros? ")) * 1.0
        cents = int(input("How many cents? ")) * 0.01
        total_inserted = euros +cents
        return total_inserted

    def check_transaction(self, cost, total_inserted):
        if total_inserted >= cost:
            if total_inserted > cost:
                change = total_inserted - cost
                print(f"Here is €{change:.2f} in change.")
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False

    def serve_coffee(self, coffee_type):
        if coffee_type == "espresso":
            self.make_coffee(coffee_type, 1.50, 50, 0, 18)
        elif coffee_type == "latte":
            self.make_coffee(coffee_type, 2.50, 200, 150, 24)
        elif coffee_type == "cappuccino":
            self.make_coffee(coffee_type, 3.00, 250, 100, 24)
        else:
            print("Invalid coffee type. Please select espresso, latte, or cappuccino.")

    def check_resource_alert(self):
        if self.water < 50:
            print("Alert: Low water. Please refill.")
        if self.milk < 50:
            print("Alert: Low milk. Please refill.")
        if self.coffee_beans < 20:
            print("Alert: Low coffee beans. Please refill.")

# Main program
machine = CoffeeMachine(1000, 1000, 1000, 0)

while True:
    action = input("What would you like? (espresso/latte/cappuccino/off/report): ").lower()

    if action == "off":
        machine.turn_off()
    elif action == "report":
        machine.get_report()
    elif action in ["espresso", "latte", "cappuccino"]:
        machine.check_resource_alert()
        total_inserted = machine.insert_coins()
        if machine.check_transaction(2.50, total_inserted):
            machine.serve_coffee(action)
            machine.get_report()
    else:
        print("Invalid command. Please select a valid option.")
       
