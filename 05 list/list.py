# list, tupule, dictionary, set
# a = [12, 67, 78]  # list
# b = {12, 67, 78}  # set
# c = (12, 67, 78)  # tupule
  # list
# a = []
# list has hetrogenous feature
# you can store anything inside the list
# list can also store duplicates
#

# list is mutable i.e. you can change anything

#c = [1,2,3,4.5,5,6,7,]
# you can change 4.5 to 4 as it is mutable

l = [10,20,30,40,50]
print (l[:3]) # list indexing and slicing

a =[10,20,30,40,50]
a[0] = 11
print (a)

# deep copy and shallow copy
a = [10,20,30,40]

b = a    # reference copy

a = [10,20,30,40]
b = a.copy() # shallow copy

# deep copy

# import copy
a = [10,20,30,40]
b = copy.deepcopy(a)
b [0] = 100

print (a)
print (b)

# transversing method 1
a = [10,20,30,40,50]
for i in a:
    print (i)

# # transversing method 2 
a = [10,20,30,40]
for i in range (len(a)):
    print (a[i])

# list method
# help (list)

a = [10,20,30,40]
a.append (50)
print (a.count (10))
print (a)
print (a.index(10))
a.insert(2,25)
print(a)

# create a list of numbers, then calculate and print the total sum and average
a = [10,20,30,40,50]
sum = 0
count = 0
for i in (a):
    sum = sum + i
    count = count + 1
average = sum / count
print (sum)
print (average)


# find the largest element in the list along with its list
a = [45,12,78,65,98,42,56,78]
largest = a [0]
index = 0
for i in range (len(a)):
    if a [i] > largest:
        largest = a[i]
        index = i
print (f"your largest number is {largest} at index {index}")

# identify  the second largest element in the list without sorting directly

check if the list is sorted or not (increasing)
a = [1,2,3,4,5,6,7]
element = a [0]
for i in range (len(a) - 1):
    if a[i] < a[i + 1]:
        continue

    else:
        print("your list is not sorted in ascending order")
        break
else:
    print("your list is sorted")
   


# Left rotation by 1

a = [10,20,30,40,50,60,70]
b = a.copy()
a [len (a) - 1] = a[0]
for i in range(1 ,len(a)):
    a[i - 1] = b [i]

 print (a)
for i in range(len(a) - 1):
     a[i], a[i + 1] = a[i + 1], a [i]
print (a)

# right rotation by 1
for i in range (len(a) - 1, 0, -1):
    a[i], a[i - 1] = a[i - 1], a[i]
print (a)

# rotation by k times
a =[ 10, 20, 30, 40, 50, 60, 70]
b = int(input("enter the times you want the  rotation"))
for i in range (b):
    for i in range(len(a)-1):
        a [i], a [i + 1] = a [i + 1], a [i]
print (a)



# reverse the list

a =[10,20,30,40,50]
b = []
for i in range (len (a) - 1):
    print (i)

popped = a .pop()
print(a)
print (popped)
#a.clear()
