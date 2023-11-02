# Backstory:
You've been hired as a software developer by a small coffee shop named "CodeBrew." They've tasked you with building a virtual coffee machine that can make a variety of coffee types. The machine should keep track of its resources (water, milk, coffee beans) and let the user know when it's time to refill.

# Objective:
Write a Python program to simulate a coffee machine using classes and object-oriented programming concepts.

Your program should be able to take user inputs, make coffee, display a report, alert the user when resources are low, and demonstrate the functionality of the CoffeeMachine class.

# Task:

1) COMMAND LINE INTERFACE (CLI): 
- Implement A CLI that shows the user available options of the coffee machine class (example: make late, show resources).
*NOTE:* to do this you will have to implement a while loop 

2) CLASS: Create a CoffeeMachine class that has the following attributes and methods:

**Class Attributes/Variables:**
- water: Initial amount of water (in milliliters).
- milk: Initial amount of milk (in milliliters).
- coffee_beans: Initial amount of coffee beans (in grams).
- money: Initial amount of money (in dollars).
**Methods/Functions:**
- *__init__*(self, water, milk, coffee_beans, money): Initialize the coffee machine with the specified resources.
- *get_report(self)*: Display a report showing the current resource levels and money.
- *turn_off(self):* Turn off the coffee machine, ending the program.
- *check_resources(self, water_needed, milk_needed, beans_needed):* Check if the machine has enough resources for the requested coffee.
- *make_coffee(self, coffee_type, cost, water_needed, milk_needed, beans_needed):* Make coffee of the specified type, subtracting the required resources. The machine should support at least five coffee types, each with different resource requirements.
- *insert_coins(self):* Prompt the user to insert coins and calculate the total amount.
- *check_transaction(self, cost):* Check if the user has inserted enough money to purchase the drink.
- *give_change(self, cost):* If the user has inserted too much money, offer change and update the machine's money.
- *serve_coffee(self, coffee_type):* Serve the coffee to the user and update the resource levels.
- *check_resource_alert(self):* Alert the user when resources are low.



# The program should:
- Create an instance of the CoffeeMachine class with initial resource amounts and zero money.
- Continuously prompt the user by asking, "What would you like? (espresso/latte/cappuccino/off/report):"
- Check the user's input and decide what to do next.
- Display the prompt each time an action has completed.
- Allow the user to turn off the machine by entering "off."
- Allow the user to print a report by entering "report."
- Check if there are enough resources to make the selected coffee type, and if so, guide the user through the process of making the coffee.

# Summary
This exercise is designed to allow you to apply your knowledge of classes, attributes, and methods in Python to build an interactive coffee machine simulation. It simulates real-world interactions and covers a variety of concepts, including input handling, resource tracking, and transaction processing. Everyone will have their own solution to this task. feel free to experiment with different concepts within the OOP paradigm. 