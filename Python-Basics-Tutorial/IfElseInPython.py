# Logical Operators = and , or , not
a= 15
b= 20
c= 5
# true and true = true
# true and false = false
# true or false = true
if(a>b or a>c) :
    print("A is Bigger")
elif(b>a and b>c) :
    print("B is Bigger")
else:
    print("C is Bigger")

d = 50
e = 55

if not (d>e) :
    print("D is bigger")
else:
    print("E is Bigger")
