# if else question practise
# compare Two number--take two user input and determine which number is greater
'''
a = float(input("enter the first number :"))
b = floatt(input("enter the second number :"))
if ( a == b):
    print(" both number are equal")
elif( a > b):
    print("a is the greatest")
else:
    print("b is the greatest")
'''

# greet by Gender( m / f)
# accept a gender input ('m' or 'f' to greet like hello sir or hello ma'am)
'''
gen = str(input("enter your gender : "))
if (gen == 'm'):
    print("hello sir")
else:
    print("hello ma'am ")
   ''' 

# Gender with case handling
# make the gender check case- insensitive('m' , 'M',  'f', 'F')
'''
gen = str(input("enter your gender : "))
if (gen == 'm' or gen == 'M'):
    print("Hello sir")
elif(gen == 'f' or gen == 'F') :
    print("hello ma'am")
else:
    print("wrong input")
'''

# even or odd checker
'''
a = int(input("write your number"))
if (a % 2 == 0):
    print("even number")
else:
    print("odd number")
'''
# voting Eligibility
# input name and age . if age >= 18 print eligible to vote . if not , print how many years are left to vote
'''
name = input("enter your name : ")
age = int(input("enter your age"))
if (age >= 18):
    print("eligible to vote")
else:
    print(f"{18 - age} years left to vote")
'''

# Day number to Day name
#take any integer 1 - 7 and print corresponding weekdays. handle input values too
'''
num = int(input("enter the number : "))
if (num == 1 ):
    print (f"Today is monday")
elif (num == 2 ):
    print (f"Today is tuesday")
elif (num == 3 ):
    print (f"Today is wednesday")
elif (num == 4 ):
    print (f"Today is thursday")
elif (num == 5 ):
    print (f"Today is friday")
elif (num == 6 ):
    print (f"Today is saturday")
elif (num == 7 ):
    print (f"Today is sunday")
else:
    print("wrong input")
    '''

# greatest of three number
# accept three number and find the greatest among them also find if twi are equal or if htree are equal
'''
a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

if ( a == b & b == c):
    print ("all numbers are equal")
if ( a == b or b == c or c== a):
    print("any two numbers are equal")

if (a > b & a > c):
    print(f"{a} is the greatest")
elif (b > a & b > c):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")

'''

# leap year checker
# input a year and if its a leap year or not using proper rule: divisible by 4 , not by 100 unless divisible by 400
'''
year = int(input("enter the year"))
if (year % 100 == 0  & year % 4 == 0):
    print(f"{year} is a leap year")
elif (year % 100 != 0 & year % 4 == 0):
    print(f"{year} is a leap year")
else :
    print (f"{year} is not a leap year")
'''


# shop discount calculator
# ask for purchase amount. apply discount based on threshold: e.g above 1000 10 percent off above 5000 20 percent off. print final bill
'''
amt = float(input("enter your purchase amount : "))
if (amt <= 1000):
    print(f"your final bill is {amt}")
elif (1000 < amt < 5000):
    print(f"your final bill is {amt - (amt * 10) / 100}")
else:
    print(f"your final bill is {amt - (amt * 20) / 100}")

'''

# accept a single alphabebt character and check if its a vowel or consonant . and also handle invalid character
'''
ch = chr(input("enter your alphabet : "))
if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(f"{ch} is vowel")

'''

char = input ("enter your character")

if char in "aeioiuAEIOU" :
    print("its a vowel")
else:
    print("its a consonant")
