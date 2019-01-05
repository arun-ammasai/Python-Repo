#Encapsulation
#Computer 

class Computer :
    def __init__(self):
        self.__maxprice=500

    def sell(self):
        print("Selling Price {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price;

comp = Computer()
comp.sell()

#Update the price
comp.__maxprice = 1000
comp.sell()

# using setter
comp.setMaxPrice(1000)
comp.sell()


