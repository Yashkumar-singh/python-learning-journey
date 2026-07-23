# while (condition):     syntax

a = 0

while a < 10:
    a = a + 1
    print (a)

# print number from n to 0
n = int(input("enter the number : "))
while n >= 0:
    print (n)
    n = n-1


# continue --- stops a particular iteration whenever continue is encountered, it will not stop the loop
for i in range(11):
    if i == 6:
        continue
    print (i)

# else --- if a break keyword is encountered else block will not execute but if no break is encounterd else block will definitely execute
for i in range (1,6):
    if i == 8:
        break
    print (i)
else:
    print("no break executed") 

# continuous number input untill 0 is  entered and then sum of all input 
a = int(input())
sum = 0
while a > 0 or a < 0:
    sum = sum + a
    a = int(input())
print (sum)


# print product of the digit of a  given number 
a = int(input())
product = 1
if a == 0 :
    product = 0
if a < 0:
    a = -a
while a > 0:
    b = a % 10
    product = product * b
    a = a // 10
print (product)
