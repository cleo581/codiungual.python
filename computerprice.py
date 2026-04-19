class computer:
    def __init(self):
        self.__price =900
    def sell(self):
        print("selling price is", self.__price)
    def setprice(self, price):
        self.__price =price
c=computer()
c.sell()
c.__price=2000
c.sell()
c.setprice(5000)
c.sell()