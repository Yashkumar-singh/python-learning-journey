# Solid Square
n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    for j in range (1, n + 1):
        print("*" , end = "")
    print()

# Hollow Square
n = int(input("enter the number of rows: "))
for i in range (1 , n+1):
    for j in range (1, n + 1):
        if j == 1 or j == n or i == 1 or i == n:
            print("*", end = " ")
        else:
            print (" ", end = " ")
    print()

# Solid Rectangle

a = int(input("Enter the length of rectangle: "))
b = int(input("enter the breadth of rectangle: "))
for i in range (1, a + 1):
    for j in range (1, b + 1):
        print("*", end = " ")
    print()

# Hollow Rectangle
a = int(input("enter the size of length : "))
b = int(input("Enter the size of breadth: "))
for i in range (1, a + 1):
    for j in range (1, b + 1):
        if i ==1 or i == a or j == 1 or j== b:
            print ("*", end = " ")
        else:
            print(" ", end = " ")
    print ()

# Left Half Pyramid

n = int(input("enter the number: "))
for i in range (1 , n + 1):
    for j in range (1, i + 1):
        print ("*", end = "")
    print ()
        
# Right Half Pyramid

n = int(input("enter the number: "))
for i in range (1, n + 1):
    for k in range (i, n):
        print (" ", end = "")
    for j in range (1, i + 1):
        print ("*", end = "")
    print ()
        
# Inverted Left Half Pyramid

n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    for j in range (n, i-1, -1):
        print ("*", end = "")
    print ()

# Inverted Right Half Pyramid
n = int (input ("enter the number: "))
for i in range (1 , n + 1):
    for k in range (i, 0 , -1):
        print(" ", end = "")
    for j in range (n, i - 1, -1):
        print ("*", end = "")
    print ()

# Floyd's Triangle
n = int(input ("Enter the number of rows: "))
sum = 0
for i in range (n + 1):
    for j in range (1, i + 1):
        sum += 1
        print (sum, end = " ")
    print ()
        
# Pascal Triangle 
n = int(input ("enter the number of rows"))
previous_list = []
for i in range (1, n + 1):
    current_list = []
    for k in range (i, n):
        print ("", end = " ")
        
    for j in range (1, i + 1 ):
        
        if j == 1 or j == i:
            print (1, end = " ")
            current_list.append(1)
        
        else:
            
            b = previous_list[j - 2] + previous_list[ j - 1]
            current_list.append(b)
            print (b, end = " ")
    print ()
    previous_list = current_list

# number pattern
# 1
# 22
# 333
# 4444

n = int(input("enter the number of rows:  "))
total = 0
for i in range (1, n+1):
    total += 1
    for j in range (1, i + 1):
        print (total, end = "")
    print()
    


# 1
# 12
# 123
# 1234

n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    total = 0
    for j in range (1, i + 1):
        total += 1
        print(total, end = "")
    print ()


# 1
# 21
# 321
# 4321

n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    for j in range (i, 0, -1):
        print (j, end = "")
    print()

# 12345
# 1234
# 123
# 12
# 1

n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for j in range (1, i + 1):
        print(j, end = "")
    print()

# 55555
# 4444
# 333
# 22
# 1

n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for j in range (1, i+1):
        print(i, end = "")
    print()

# A
# AB
# ABC
# ABCD

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    x = 65
    for j in range (1, i + 1):
        print(chr(x), end = "")
        x += 1
    print ()

# A
# BB
# CCC
# DDDD


n = int(input("Enter the number of rows: "))
x = 65
for i in range (1, n + 1):
    for j in range (1, i + 1):
        print(chr(x), end = "")
    x += 1
    print()
        

# ABCDE
# ABCD
# ABC
# AB
# A

n = int(input("Enter the number of rows: "))
for i in range (n, 0 , -1):
    x = 65
    for j in range (1, i + 1):
        print(chr(x), end = "")
        x += 1
    print()

# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for j in range (i, n + 1):
        x = 65
        x += j - 1
        print(chr(x), end = "")
    print()

# 1
# 23
# 456
# 78910

n = int(input("Enter the number of rows:"))
total = 0
for i in range (1, n + 1):
    for j in range (1, i + 1):
        total += 1
        print(total, end = "")
    print ()

# Full Pyramid


n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    for k in range (1, n - i + 1 ):
        print(" ", end = " ")
    for j in range (1, 2 * i ):
        print ("*", end = " ")
    print()



# Hollow Pyramid
n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    for k in range (1, n - i + 1):
        print (" ", end = " ")
    for j in range (1, 2 * i):
        if j ==1 or j == ((2 * i)-1) or i == n:
            print ("*", end = " ")
        else:
            print (" ", end = " ")
    print ()

# Inverted Full Pyramid

n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for k in range (i, n+1):
        print (" ", end = " ")
    for j in range (1 , 2 * i):
        print ("*", end = " ")
    print ()

# Hollow Inverted Pyramid

n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for k in range (i, n + 1):
        print (" ", end = " ")
    for j in range (1, 2 * i):
        if i == n or i == 1 or j == 1 or j == (2 * i) - 1:
            print ("*", end = " ")
        else:
            print (" ", end = " ")
    print ()

# Diamond
n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    for k in range (1, n - i + 1):
        print (" ", end = "")
    for j in range (1, 2 * i):
        print ("*", end = "")
    print ()
x = 3 
for  i in range (n+1, 2 * n ):
    for k in range (n + 1 , i + 1):
        print (" ", end = "")
        
    for l in range (1, ((2 * n) -(x) ) + 1 ):
        print ("*", end = "")
    print ()
    x += 2

n = int(input("enter the number of rows: "))
for i in range (1 , n + 1):
    for k in range (1, n - i + 1):
        print(" ", end = "")
    for j in range (1, 2 * i ):
        print ("*", end = "")
    print()
for i in range (n - 1, 0, -1):
    for k in range (n-1, i-1, -1):
        print (" ", end = "")
    for l in range (1, 2 * i):
        print ("*", end = "")
    print ()


# Hollow Diamond

n = int(input("enter the number of rows: "))
for i in range (1, n + 1):
    for k in range (1, n - i + 1):
        print (" ", end = "")
    for j in range (1, 2 * i ):
        if i == n or i == 1 or j == 1 or j == 2 * i - 1:
            print("*", end = "")
        else:
            print (" ", end = "")
    print ()
    
for i in range (n - 1, 0, -1):
    for k in range (n - 1, i - 1, -1):
        print (" ", end = "")
    for j in range (1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 1:
            print ("*", end = "")
        else:
            print (" ", end = "")
    print ()

# Hourglass
n = int(input("enter the number of rows: "))
for i in range (n, 0, -1):
    for k in range (n, i - 1, -1):
        print (" ", end = "")
        
    for j in range (1, 2 * i  ):
        print ("*", end = "")
    print ()
for i in range (2, n + 1):
    for k in range (0, n - i + 1 ):
        print (" ", end = "")
    
    for j in range (1, 2 * i):
        print ("*", end = "")
    print ()

# Hollow Hourglass
n = int(input("enter the number of rows:"))
for i in range (n, 0, -1):
    for k in range (n, i - 1, -1):
        print (" ", end = "")
    for j in range (1, 2 * i):
        if i == 1 or i == n or j == 1 or j == 2 * i - 1 :
            print ("*", end = "")
        else:
            print (" ", end = "")
    print ()
    
for i in range (2 , n + 1):
    for k in range (0, n - i + 1):
        print (" ", end = "")
    for j in range (1, 2 * i):
        if i == n or j == 1 or j == 2 * i - 1:
            print ("*", end = "")
        else:
            print (" ", end = "")
    print ()
