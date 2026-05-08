import sys

print(sys.version)


true_boolean=True

flase_boolean=False


for x in range(10):
    print(x,end=" ")

    
print()
print("I am and the ",25)

num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

print(type(num1))
print(type(num2))


print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)

#check the enviornment of the deployment

env=input("Enter The Enviornment please To Deploy")

print("The Envioenment is " + env)

if env=='prod':
    print("Deploy on Working Days Except Sat/Sun")
elif env=='stg':
    print("Deployment can be possible in any day")
else:
    print("The Deployment can not be done will see on monday")