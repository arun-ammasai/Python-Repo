#data = [x for var in range [1,10]]
numbers = [x for x in range(1,11)]
print(numbers)
print(type(numbers))
oddNumbers = [x for x in range(1,51) if x%2!=0]
print(oddNumbers)
evenNumbers = [x for x in range(1,51) if x%2==0]
print(evenNumbers)

names =["John","Dennis","Daniel"]
#[4,"JOHN","john"]
output = [[len(d),d.upper(),d.lower()] for d in names]
print(output)
