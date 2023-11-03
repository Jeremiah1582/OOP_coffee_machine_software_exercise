from termcolor import colored
import time


# define class
class coffeeMachine:
    def __init__(self):
        self.cash = 0
        self.machineMoney = 100  # €
        self.water = 1000  # ml
        self.oatMilk = 1500  # ml
        self.coffeeBeans = 500  # grams
        self.machineOptions = {
            "blackCoffee": float(1.50),
            "latte": float(4.50),
            "cappuccino": float(3.90),
            "show resources": "",
            "cancel order": "",
            "turn off machine": "",
        }

    # get report magic function
    def __str__(self):
        return colored(
            f"\n ------resource report------- \n water: {self.water}ml \n oatMilk: {self.oatMilk}ml \n CoffeeBeans: {self.coffeeBeans}g \n Money_in_Machine: €{self.machineMoney} \n",
            "yellow",
        )

    # customer choice functions
    def makeBlackCoffee(self, payment):
        change_or_msg = self.calc_change(payment, (self.machineOptions["blackCoffee"]))
        if self.is_resource_low():
            return colored("\n resources are too low to make \n", "on_red")

        if not isinstance(change_or_msg, float):
            return colored("\n insert correct Payment ! \n ", "red")

        self.water = self.water - 80
        self.oatMilk = self.oatMilk - 150
        self.coffeeBeans = self.coffeeBeans - 20
        self.machineMoney = self.machineMoney + self.machineOptions["blackCoffee"]

        return colored(
            f"\n enjoy your Black Coffee, your change is: €{change_or_msg:.2f} \n",
            "blue",
        )

    def makeLatte(self, payment):
        change_or_msg = self.calc_change(payment, (self.machineOptions["latte"]))
        if self.is_resource_low():
            return colored(
                "\n resources are too low to make Order, refill machine \n ", "on_red"
            )
        if not isinstance(change_or_msg, float):
            return colored("insert correct Payment !", "red")

        self.water = self.water - 80
        self.oatMilk = self.oatMilk - 150
        self.coffeeBeans = self.coffeeBeans - 20
        self.machineMoney = self.machineMoney + self.machineOptions["latte"]

        return colored(
            f"\n enjoy your Latte, your change is: €{change_or_msg:.2f} \n", "blue"
        )

    def makeCappuccino(self, payment):
        change_or_msg = self.calc_change(payment, (self.machineOptions["cappuccino"]))
        if self.is_resource_low():
            return colored("\n resources are too low to make Ord, er \n", "on_red")

        if not isinstance(change_or_msg, float):
            return colored("\n insert correct Payment ! \n", "red")

        self.water = self.water - 80
        self.oatMilk = self.oatMilk - 150
        self.coffeeBeans = self.coffeeBeans - 20
        self.machineMoney = self.machineMoney + self.machineOptions["cappuccino"]

        return colored(
            f"\n enjoy your Cappuccino, your change is: €{change_or_msg:.2f} \n", "blue"
        )

    def refund(self, payment):
        print(colored(f"\n your payment of {payment} is being returned \n", "green"))
        time.sleep(1.5)
        return payment

    # machine backend functions
    def calc_change(self, payment, cost):
        if cost > payment:
            return f"please put in the correct amount"
        total_change = float(payment - cost)
        return total_change

    def is_resource_low(self):
        if (
            self.water
            < 100 | self.oatMilk
            < 100 | self.coffeeBeans
            < 50 | self.machineMoney
            < 20
        ):
            return True
        return False
