class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a < other.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if self.a == other.a:
            return "ob1 is equal to ob2"
        else:
            return "ob1 is not equal to ob2"
ob1=a(10)
ob2=a(20)
print("passes value of ob1 and ob2 ",ob1.a,ob2.a)
print(ob1<ob2)
ob3=a(10)
ob4=a(10)
print(ob3==ob4)