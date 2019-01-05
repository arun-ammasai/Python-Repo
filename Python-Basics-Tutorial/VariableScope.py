a= 100 #50 #75
#Global = you cannot modify/override
def test1():
    global a
    a=50
    print(a)

def test2():
    global a
    #global a = 50
    a =75;
    print(a)

test1()
test2()
print(a)
