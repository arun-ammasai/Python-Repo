#Inheritance
# Parent = Child
class Bird :
    def __init__(self) :
        print("Bird is ready")

    def who() :
        print("Bird")

    def swim(self) :
        print("Swim Faster")

class Penguin(Bird) :
    def __init__(self) :
        super().__init__()
        print("Penguin is Ready")

    def who(self) :
        print("Penguin")

    def run(self) :
        print("Run faster")

penguin = Penguin()
penguin.who()
penguin.swim()
penguin.run()



    
