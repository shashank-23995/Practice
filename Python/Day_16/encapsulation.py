class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price
    
import pdb; pdb.set_trace()
c = Computer()
c.sell()

# change th price
c.__maxprice = 100
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()