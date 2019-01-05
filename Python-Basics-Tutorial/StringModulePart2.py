# Getting input from user [input()]
name = input("Enter your name :")
lives = input("I'm from :")
hobbies = input("Enter your hobbie :");
#print(name,lives,hobbies)
output="My name is {} and I'm from {} and love to {}";
print(output.format(name,lives,hobbies))
