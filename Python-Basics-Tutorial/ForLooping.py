#Syntax for var in range
'''for num in range(11,1) :
    print(num)
for let in "PYTHON" :
    print(let)
for li in ["John","Dennis","Daniel"] :
    print(li) '''

emp = {"Male":["John","Dennis","Daniel"],
       "Female":["Nancy","Mathew","Liza"]}
print(emp)

for key in emp.keys() : # ["Male","Female"]
    print(key)
    print(emp[key])
    for name in emp[key] : #['John', 'Dennis', 'Daniel']
        if("a" in name) :
            print(name)
        
