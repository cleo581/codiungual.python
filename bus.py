class vehicle:
    def __init__(self,capacity):
        self.capacity=capacity
    def display(self):
            return self.capacity*100
class bus(vehicle):
    def __init__(self,capacity):
        super().__init__(capacity)

    def fare(self):
        basefare = self.display()
        maintence_charge = basefare*0.10
        totalfare = basefare +maintence_charge
        return totalfare
bus  = bus(50)
print("total Bus fare is",bus.fare())

    