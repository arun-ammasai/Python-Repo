# get user email
mail = input("Please enter your email ID :")
print(mail)
# arun.ammasai@outlook.com
# extract name from email
name =mail[:mail.index("@"):]
print(name)
host = mail[mail.index("@")+1:mail.index("."):]
#email[11:4]
print(host)
# extract email host

output="Username is {1} and mail provider is {0}"
print(output.format(host,name))
