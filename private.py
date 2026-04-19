class myClass:
    __privateVar = 27;
    def __privatemethod(self):
        print("this is a private method")
    def hello(self):
        print("private variable is ",myClass.__privateVar)
ob1 = myClass()
ob1.hello()
ob1.__privatemethod()