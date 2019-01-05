# Write a method to validate username and password
# get the inputs from user
# check username and password are admin
username =input("Enter your Username :").strip()
password =input("Enter your Password :").strip()

def loginValidation(uname,upass) :
    print("User Login Details :",username,password)
    if(username=="admin" and password=="admin") :
        return "SUCCESS"
    else :
        return "FAILURE"

response = loginValidation(uname=username,upass=password)
print(response)
