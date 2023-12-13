class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)
    def opening_hours(self):
        print("Opening hours: " + self.opening_hours())
