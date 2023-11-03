from class_coffeeMachine import coffeeMachine


code_coffee = coffeeMachine()

# CLI
while True:
    
    print("------Select Your Order-------")
    for i, (k, v) in enumerate(code_coffee.machineOptions.items()):
        print(f"{i+1}) {k}  {'€'+str(v) if isinstance(v,float) else ''}")

    choice = int(
        input(
            f"please select from options 1-{len(code_coffee.machineOptions.items())}: "
        )
    )
    print("-----------------------------")

    def switchboard(num):
        if num == len(code_coffee.machineOptions.items()):
            print("turning off machine...")
            exit()
        elif num == 4:  # print resources __str__
            print(code_coffee)
        elif num == 5:  # print resources __str__
            print(code_coffee)
            code_coffee.refund(0)
        else:
            euro_input = int(input("insert Euros: ")) * 1
            cent_input = int(input("insert Cents: ")) * 0.01
            total_cash = float(euro_input + cent_input)

            mySwitch = {
                1: code_coffee.makeBlackCoffee,
                2: code_coffee.makeLatte,
                3: code_coffee.makeCappuccino,
                # 4) if statement catches 4
                # 5: if statement catches 5
                # 6: "turn off machine",
            }

            result = mySwitch[num]  # this is a reference to the function
            if result is not None:
                print(result(total_cash))
            else:
                print("invalid option")

    print(switchboard(choice))
