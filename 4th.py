import random

import itertools

name=input("enter your name :")

print("hey" +name+"!!!,welcome to password generator")

x=int(input("How many number you want in your password"))
num=[i for i in range(10)]
a=random.sample(num,x)

y=int(input("how many latters you want in your password"))
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=random.sample(alp,y)

z=int(input("how many symbols you want in your password "))
sbl="!@$%^&*_+=-<>"
c=random.sample(sbl,z)

print("This is your password as per your requirement:")
var=list(itertools.chain(a,b,c))
final = random.sample(var,len(var))
for i in range(len(final)):
    print(final[i])