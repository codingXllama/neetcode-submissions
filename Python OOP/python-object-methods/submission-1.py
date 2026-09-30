class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -=1
        return f"Fluffy has been fed.\nFluffy's hunger level: {self.hunger}"

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
print(my_pet.feed())
print(my_pet.feed())
print(my_pet.feed())