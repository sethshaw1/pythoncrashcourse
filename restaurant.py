
class Restaurant:
    """An attempt to model a restaurant"""
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant.")
        
    def open_restaurant(self):
        print(f"{self.name} is now open!")
        
    def set_number_served(self, served):
        self.number_served = served
        
    def increment_number_served(self, served):
        self.number_served += served
        
restaurant_1 = Restaurant("Nando's", "Portuguese")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_1.set_number_served(23)
restaurant_1.increment_number_served(22)
restaurant_1.increment_number_served(22)
print(restaurant_1.number_served)

