# print hello world n times... use a loop to repeat a print statement ("hello world") based on user count
n = int(input("write the number of time you want to repeat : "))
for i in range(1,n+1,1):
  print("Hello World")


# print number from 1 to n
# display number in increasing order from 1 to n
n = int(input("enter the number: "))
for i in range (1, n + 1 , 1):
    print(i)

# print number from n to 1:
n = int(input("enter the number : "))
for i in range (n , 0 , -1):
    print(i)

# Sum of natural number from 1 to n:
n = int(input("Enter the number : "))
sum = (n * (n+1)) / 2
print(sum)

## another method
n = int(input("Enter the number : "))
sum = 0
for i in range(1 , n+1, 1):
    sum = sum + i
print(sum)

# you have given two integer, start and end of integer. print all prime number falling within this range
a, b = map(int, input().split())
prime = 0
for i in range (a, b+1):
    if i < 2:
        continue
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        print (i, end = " ")
        prime = prime + 1
if prime == 0:
    print ("No prime numbers")

# # factorial of a number using loop
n = int(input("enter the number : "))
fact = 1
for i in range (1 , n+1 , 1):
    fact = i * fact
print (fact)

# Sum of even and odd number in Range
# from 1 to n find an dprint the sum of all even and all odd number
n = int(input("write the number : "))
odd_number = 0
even_number = 0
for i in range(1, n + 1 , 2):
    odd_number = odd_number + i
print(f" sum of given odd number in the given range is {odd_number}")
for i in range(2, n + 1 , 2):
    even_number = even_number + i
print(f"sum of given even number in the given range is {even_number}")


# print all factors of a number:
# display all number that divide the input exactly

n = int(input("enter your number : "))

for i in range (1 , n+1):
    if (i % n == 0):
        factor = i 
    print(factor)

# count uppercase and lowercase

a = str(input())

uppercase = 0
lowercase = 0

for i in range (len(a)):
    if a[i] in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
        uppercase = uppercase + 1
    if a [i] in 'a b c d e f g h i j k l m n o p q r s t u v w x y z':
        lowercase = lowercase + 1
print (f"Uppercase: {uppercase}")
print (f"Lowercase: {lowercase}")

# count even and odd digit number
a = int(input())
even = 0
odd = 0
if a == 0:
    even = 1
elif a < 0:
    a = -a 
while a > 0:
    b = a % 10
    if b % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    a = a // 10
print (f"Even: {even}")
print (f"Odd: {odd}")

# print palindrome number
a, b = map(int, input().split())
palindrome = 0 
for i in range (a, b+1):
    rev = 0
    if i < 0:
        continue
    copy = i
    while i > 0:
        b = i % 10
        rev = rev * 10 + b
        i = i // 10
    if rev == copy:
        print (copy, end = " ")
        palindrome = palindrome + 1
if palindrome == 0:
    print("No palindrome numbers")
  
# number with exactly 3 factor
a = int(input())
for i in range (1,a+1):
    factor = 0
    for j in range (2,i ):
        if i % j == 0:
            factor = factor + 1
    if factor == 1:
        print (i, end = " ")

# armstrong number checker
a = int(input())
number = 0
digit = 0
if a < 0:
    a = -a
copy1 = a
copy2 = a
while a > 0:
    b = a % 10
    number = number + 1
    a = a // 10
while copy1 > 0:
    c = copy1 % 10
    digit = digit + (c ** number)
    copy1 = copy1 // 10
if copy2 == digit:
    print ("Armstrong")
else:
    print ("Not Armstrong")

# print largest digit
a = int(input())
largest_digit = 0
if a < 0:
    a = -a 
while a > 0:
    b = a % 10
    if b > largest_digit:
        largest_digit = b
    a = a // 10
print (largest_digit)


# strong number check
a = int(input())
copy = a
sum = 0
if a < 0:
    a = -a 
while a > 0:
    factorial = 1
    b = a % 10
    for i in range (b , 0, -1):
        factorial = factorial * i
    sum = sum + factorial
    a = a // 10
if sum == copy:
    print ("Strong Number")
else:
    print("Not Strong Number")




