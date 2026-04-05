class parot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
parot1=parot("tom",15)
parot2=parot("jerry",76)
print("species of tom =",parot1.species)
print("jerry is also a ",parot.species)
print("age of tom is=",parot1.age)
print(parot2.age)
        