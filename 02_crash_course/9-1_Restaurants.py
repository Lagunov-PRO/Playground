class Restaurants:

    def __init__(self, name, cousine):
        self.name = name
        self.cousine = cousine

    def describe_restaurant(self):
        print(self.name, self.cousine)


mc = Restaurants('McDonalds', 'burgers')

Restaurants.describe_restaurant(mc)

