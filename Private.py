class CoffeeMachine():
    WATER_LEVEL = 100

    def start_machine(self):
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add water!")
            return False

    def boil_water(self):
        return "boiling..."

    def make_cofee(self):
        if self.start_machine():
            self.WATER_LEVEL -= 20
            print(self.boil_water())
            print("Coffee is ready!")

machine = CoffeeMachine()
for i in range(0, 5):
    machine.make_cofee()