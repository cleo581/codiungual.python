class dog:
    species="canis lupus familiaris"
    def __init__(self, name, age=0):
        self.name = name
        #class atritubit,specific to the class
        self.age = age
    
    def bark(self, sound):
        return self.name + " sound like " + sound
    
        def __str__(self):
            return f"{self.name} is {self.age} years old"
    
    tiger=("tiger",15)
    print(tiger)
    bark=("auf")
    print(bark)
    dog2=("tom",15)
    print(dog2)
    bark2=("woof")
    print(bark2)
 
dog1="golden retriever"
print(dog1)
tiger=("golden retriever")
#a dog class example to understand object oriented programing
class goldenretriver:
    pass
class husky:
    pass
class poodle:
    pass