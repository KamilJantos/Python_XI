

class Fridge:
    def __init__(self):
        self.temperature = 2  # in celsius

    def __str__(self):
        return f'fridge temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the fridge's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the fridge's temperature by {amount} degrees")
        self.temperature -= amount
