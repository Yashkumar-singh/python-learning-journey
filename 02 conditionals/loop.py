# loop --- it is used when we want to perform repetitive task
# types of loops -- For loop, while loop
# for loop is used when we know till where you wanna go
# while loop is used with a condition

print("helllo How are you") 

# suppose if you want to print this number thousand times then we use loops

# for loop
# Range function has three thing i.e. atart stop and step
ran = range(1,11,1)
print(ran)

for i in ran:
    print(i)
    
for i in ran:
    print("HELLOw HOW ARE YOU")

# ANOTHER WAY TO WRITE THE SAME THING
for i in range(1, 10, 2):
    print("mai hoon Don")

# practise question

for i in range(10 , 41 , 1):
    print(i)

# print number from -10 to 40
for i in range(-10 , 21 , 1):
    print(i)

# print number from 34 to 5
for i in range(34 , 4 , -1):
    print(i)


# print the table of 5 
n = int(input("write the number : "))
for i in range(n , n * 11 , n):
    print(i)

# loops with string
s = "Hello! how are you"
for i in s:  # first way
    print(i)

for i in range(0 ,len(s), 1):
    print(s, [i])

# default value(0 , , 1)

a = "nature"
for i in range (len(a)):
    print(a[i])
