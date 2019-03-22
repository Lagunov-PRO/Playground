class Restaurants:

    def __init__(self, name, cousine):
        self.name = name
        self.cousine = cousine

    def describe_restaurant(self):
        print(self.name, self.cousine)


mc = Restaurants('McDonalds', 'burgers')
sub = Restaurants('Subway', 'sandwiches')
br = Restaurants('Baskin Robins', 'ice-cream')

Restaurants.describe_restaurant(mc)
Restaurants.describe_restaurant(sub)
Restaurants.describe_restaurant(br)

