class vehicle:
    def __init__(self,maxspeed,mileage,name):
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.name=name
class bus(vehicle):
    pass
ob1=bus(120,14,"school bus")
print("the name of the bus is=",ob1.name)
print("the mileage of the the bus is=",ob1.mileage)
print("the maxspeed of the bus is",ob1.maxspeed)