emp = {"John":25,"Dennis":28,"Coulson":30}
print(emp)
emp1 = {"John":["Sales",20,1500],
        "Dennis":["Marketting",25,2500],
        "Coulson":["Finance",28,3500]}
print(emp1)
name = input("Enter employee Name :").strip()
#print(emp1[name][2],emp1[name][0])

emp2 = {"John":{"Department":"Sales","Age":20,"Salary":1500},
        "Dennis":{"Department":"Marketting","Age":25,"Salary":2500},
        "Coulson":{"Department":"Finance","Age":28,"Salary":3500}}
print(emp2[name]["Department"],emp2[name]["Salary"])

print(emp2.keys())
print(emp2.values())
print(emp2.items())
print(list(emp2.keys()))#[ List ]
print(list(emp2.values()))#[ List ]
listOfKeys = list(emp2.keys())
print(listOfKeys)





