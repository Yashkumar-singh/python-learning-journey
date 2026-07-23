'''
a = int(input("please provide your number: "))
b = int(input("please provide your number: "))

print (a + b)

c = int(input("please provide your number: "))
d = int(input("please provide your number: "))

print (c + d)
'''

# function is a block of code which can be called again and again
# two type of function == inbuilt function and user defined
def Greeting():  # defining
    print (" Hello ! how are you")
    return " hello ! how are you"  # return function always return statement  to calling spot

# result = Greeting ()
# print(result)
# Greeting() # calling this function
# Greeting() # calling this function
# Greeting() # calling this function
# Greeting() # calling this function

# # parameter and argument 
#  # parameters are a kind of variable we accept in our function
#  # argument are the variable or values that we pass to those parameters keyword argument, default parameters, parameters with values
def addition (a, b):
   print (a + b)
addition(12, 37)

# # to see if a given word is pallindrome or not
def pallindrome (x):
    rev = 0
    copy = x
    while x > 0:
        rev = rev * 10 + x % 10
        x = x // 10
    if rev == copy:
        print(" given number is pallindrome ")
    else:
        print("Given number is not pallindrome")
        return True
    else:
        return False

    
# print (pallindrome (123))
# print (pallindrome (33433))
# print (pallindrome (95722759))

def addition (a , b):
    print (a + b)

addition ( b = 12, a = 13) # keyword arguments

def addition (a, b, c = 14):
    print ( a + b )

addition (12, 13,)
# default value  of a parameter can be set to last

