# if else used to control the flow of the program
age = int(input("please tell your age: "))
if (age >= 18): # after if we put condition
    print("you can vote")
else:
    print("you cannot vote")

# indentation is a 5 space block used to write inside if and else
# you cannot write any condition in else statement
# pass is used when you dont want to write anything inside else is the final stop

# ternary operator
print("vote") if (age >= 18) else print("not vote")

# Elif statement
money = int(input("please give me 10,20,30 or above"))
if (money == 10):
    print("i will eat choco bar")
elif (money == 20):
    print("i will eat mango dolly")
elif(money == 30):
    print("i will take coke")
else:
    print("i will take x y z")

# using logical operator
a = 10
b = 20 
c = 30
if (a > b & a > c):
    print(" a is the greatest")
elif (b > a & b > c):
    print("b is the greatest")
else:
    print(" c is the greatest")