#Polymorphism
class Parrot :
    def fly(self) :
        print("Parrot Can Fly")

    def swim(self) :
        print("Parrot Can't Swim")

class Penguin :
    def fly(self) :
        print("Penguin Can't Fly")

    def swim(self) :
        print("Penguin Can Swim")


#Common interface
def flyingTest(obj):
    obj.fly()

def swimTest(obj):
    obj.swim()

parr = Parrot()
#parr.fly()
peng = Penguin()
#peng.fly()

flyingTest(parr)
flyingTest(peng)
print("======================")
swimTest(parr)
swimTest(peng)


