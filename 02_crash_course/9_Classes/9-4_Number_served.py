class Fastfood:

    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


mc = Fastfood('McDonalds', 'burgers')

print(mc.number_served)

mc.number_served = 5
print(mc.number_served)

mc.set_number_served(15)
print(mc.number_served)

mc.increment_number_served(3)
print(mc.number_served)

