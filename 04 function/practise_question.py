# to check the sign of a number
def check_number_sign(num):
    if num > 0:
        return ("Positive")
    elif num < 0:
        return ("Negative")
    else:
        return ("Zero")
num = int(input("enter the number")

# even number checker

def check_even(num):
    # Write your code here
    if num % 2 == 0:
        return ("Even")
    else:
        return ("Odd")
    num = (int(input("enter the number"))
    pass

# diplay multiplication of a number
def print_table(n):
    for i in range (1, 11):
        print (f"{n} x {i} = {n * i}")

  n = int(input("enter the number"))
  pass
  
#count the number of a digit:
def count_digits(n):
    
    digit = 0
    if n == 0:
        digit = 1
    elif n < 0:
        n = -n
    while n > 0:
        b = n % 10
        digit = digit + 1
        n = n // 10
    print (digit)

n = int(input("enter the number))
              
pass
              
    

# sum of first natural number

def sum_of_naturals(n):
    sum = 0
    for i in range (n+1):
        sum = sum + i
    print (sum)

n = int(input("enter the number"))

# reverse number function
def reverse_number(n):
  
    rev = 0
    copy = n
    if n < 0:
        n = -n 
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    if copy > 0:
        print (rev)
    else:
        print (-rev)
n = int (input("enter the number"))

  
