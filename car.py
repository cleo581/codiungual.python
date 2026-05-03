# Base concept: different objects responding to the same method in their own way

class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

    def description(self):
        return "BMW is known for comfort and performance."


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

    def description(self):
        return "Ferrari is known for speed and luxury."


# Polymorphism in action
def show_car_details(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("Description:", car.description())
    print("-" * 30)


# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Using the same function for different objects
show_car_details(bmw_car)
show_car_details(ferrari_car)
