from abc import ABC, abstractmethod
class abstractclass(ABC):
    def print(self, x):
        self.x = x
        print("value is =",x)

    @abstractmethod
    def task(self):
        print("we are inside an abstract class")

class  testclass(abstractclass):
    def task(self):
        print("we are inside the test class")
obj1=testclass()
obj1.task()
obj1.print(50)
