# wthr = int(input('Write how many ml of water the coffee machine has:'))
# milk = int(input('Write how many ml of milk the coffee machine has:'))
# coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
# cups_coffee = int(input('Write how many cups of coffee you will need:'))
# wthr_how = cups_coffee * 200
# milk_how = cups_coffee * 50
# coffee_how = cups_coffee * 15
# if wthr >= wthr_how and milk >= milk_how and coffee >= coffee_how:
#     a = []
#     a.append((wthr - wthr_how) // 200)
#     a.append((milk - milk_how) // 50)
#     a.append((coffee - coffee_how) // 15)
#     a.sort()
#     if a[0] > 0:
#         print(f'Yes, I can make that amount of coffee (and even {a[0]} more than that)')
#     else:
#         print('Yes, I can make that amount of coffee ')
# else:
#     a = []
#     a.append(wthr // 200)
#     a.append(milk // 50)
#     a.append(coffee // 15)
#     a.sort()
#     print(f'No, I can make only {a[0]} cups of coffee')

# water = 400
# milk = 540
# coffee = 120
# cups = 9
# money = 550
#
#
# def index(water, milk, coffee, cups, money):
#     print(f"""The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee} of coffee beans
# {cups} of disposable cups
# {money} of money""")
#
#
# def buy():
#     global water
#     global milk
#     global coffee
#     global cups
#     global money
#     want = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
#     if want == 'back':
#         pass
#     elif int(want) == 1:
#         if water < 250:
#             print('Sorry, not enough water!')
#         elif coffee < 16:
#             print('Sorry, not enough coffee!')
#         elif cups < 1:
#             print('Sorry, not enough cups!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water -= 250
#             coffee -= 16
#             cups -= 1
#             money += 4
#     elif int(want) == 2:
#         if water < 350:
#             print('Sorry, not enough water!')
#         elif coffee < 20:
#             print('Sorry, not enough coffee!')
#         elif milk < 75:
#             print('Sorry, not enough milk!')
#         elif cups < 1:
#             print('Sorry, not enough cups!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water -= 350
#             milk -= 75
#             coffee -= 20
#             cups -= 1
#             money += 7
#     elif int(want) == 3:
#         if water < 200:
#             print('Sorry, not enough water!')
#         elif coffee < 12:
#             print('Sorry, not enough coffee!')
#         elif milk < 100:
#             print('Sorry, not enough milk!')
#         elif cups < 1:
#             print('Sorry, not enough cups!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water -= 200
#             milk -= 100
#             coffee -= 12
#             cups -= 1
#             money += 6
#
#
# def fill():
#     global water
#     global milk
#     global coffee
#     global cups
#     water = water + int(input('Write how many ml of water do you want to add:'))
#     milk = milk + int(input('Write how many ml of milk do you want to add:'))
#     coffee = coffee + int(input('Write how many grams of coffee beans do you want to add:'))
#     cups = cups + int(input('Write how many disposable cups of coffee do you want to add:'))
#
#
# def take():
#     global money
#     print(f'I gave you ${money}')
#     money = 0
#
#
# def main():
#     while True:
#         action = input('Write action (buy, fill, take, remaining, exit):')
#         if action == 'buy':
#             buy()
#         elif action == 'fill':
#             fill()
#         elif action == 'take':
#             take()
#         elif action == 'remaining':
#             index(water, milk, coffee, cups, money)
#         elif action == 'exit':
#             break
#
#
#
# if __name__ == '__main__':
#     main()


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550
        self.state = "select"

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.cash} of money"""

    def display_action(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def choose_action(self, action):
        if action == "buy":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 -cappuccino, back - to main menu:")
            self.state = "buy"
        elif action == "fill":
            print("")
            self.display_fill_message("water", "ml")
            self.state = "fill_water"
        elif action == "take":
            print("\nI gave you ${}".format(self.cash))
            self.cash = 0
            self.state = "select"
            self.handle()
        elif action == "remaining":
            print(self)
            self.state = "select"
            self.handle()

    def choose_coffee(self, type_of_coffee):
        self.state = "select"
        if type_of_coffee == "1":
            self.make_coffee(water=250, beans=16, cost=4)
        elif type_of_coffee == "2":
            self.make_coffee(water=350, milk=75, beans=20, cost=7)
        elif type_of_coffee == "3":
            self.make_coffee(water=200, milk=100, beans=12, cost=6)

        self.handle()

    def use_supplies(self, r_water, r_milk, r_beans, r_cups=1):
        missed_resource = None

        if self.water < r_water:
            missed_resource = "water"
        elif self.milk < r_milk:
            missed_resource = "milk"
        elif self.beans < r_beans:
            missed_resource = "beans"
        elif self.cups < r_cups:
            missed_resource = "cups"
        else:
            self.water -= r_water
            self.milk -= r_milk
            self.beans -= r_beans
            self.cups -= r_cups

        return missed_resource

    def make_coffee(self, water=0, milk=0, beans=0, cost=0):
        missed_resource = self.use_supplies(water, milk, beans)
        if missed_resource is None:
            self.cash += cost
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough {}!".format(missed_resource))

    def display_fill_message(self, resource, measure):
        print("Write how many {} of {} do you want to add:".format(measure, resource))

    def fill_water(self, n_water):
        self.water += int(n_water)
        self.display_fill_message("milk", "ml")
        self.state = "fill_milk"

    def fill_milk(self, n_milk):
        self.milk += int(n_milk)
        self.display_fill_message("coffee beans", "grams")
        self.state = "fill_beans"

    def fill_beans(self, n_beans):
        self.beans += int(n_beans)
        self.display_fill_message("coffee", "disposable cups")
        self.state = "fill_cups"

    def fill_cups(self, n_cups):
        self.cups += int(n_cups)
        self.state = "select"
        self.handle()

    def handle(self, data=None):
        if self.state == "action":
            self.choose_action(data)
        elif self.state == "buy":
            self.choose_coffee(data)
        elif self.state == "fill_water":
            self.fill_water(data)
        elif self.state == "fill_milk":
            self.fill_milk(data)
        elif self.state == "fill_beans":
            self.fill_beans(data)
        elif self.state == "fill_cups":
            self.fill_cups(data)
        else:
            self.display_action()
            self.state = "action"

        coffee_machine = CoffeeMachine()
        user_input = ""

        while user_input != "exit":
            coffee_machine.handle(user_input)
            user_input = input()
