# linear search ---- searching for a given element by checking one by one
a = [10,20,30,40,50,60,11,58,45,26,25,14,19,18]
k = int(input("Enter the number that you want to search"))
for i in range(len(a)):
    if a[i] == k:
        print(f"element found at {i}th index")
        break
else:
    print("Element not found")


# binary search 

a = [10,20,30,32,34,36,38,40,48,50,60,80,100,101]

search = 48

start = 0
last = len(a) - 1
mid = (start + last ) // 2

while start <= last:
    if a[mid] == search:
        print(f"element found at index {mid}")
        break
    elif a[mid] < search:
        start = mid + 1
        mid = (start + last) // 2

    elif a[mid] > search:
        last = mid - 1
        mid = (start + last) // 2
else:
    print("no number exist")

# Bubble sorting -- sort the list by repeatedly swapping adjacent elements if they are in wrong order


a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]
for j in range(len(a) - 1 ):
    for i in range(len(a) - 1 - j):
        if a[i] > a[i+1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)


# selection sort ---- sort the list by repeatedly swapping adjacent elements in each pass and placing it in the correct position

a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

for i in range(len(a) - 1):
    j = i + 1
    min = i
    for k in range(j, len(a)):
        if a[k] < min:
            min = k
    a[i], a[min] = a[min], a[i]

print(a)


# split list into two halves
def split_list_in_halves(a):

    if len(a) % 2 == 0:
        first_half = a[:len(a)//2]
        second_half = a[len(a)//2:]
    else:
        first_half = a[:len(a)//2 + 1]
        second_half = a[len(a)//2 + 1:]

    return first_half, second_half

# swap first and last element
def swap_first_last_elements(numbers):
    # Write your code here
    numbers[0], numbers[len(numbers) - 1] = numbers[len(numbers) - 1], numbers[0]
    return numbers

    pass
  
# remove specific number:-
ef remove_specific_element(numbers, x):
    # Write your code here
    if x in numbers:
        numbers.remove(x)
        return (numbers)
    else:
        return numbers

# average of list element
def average_of_list_elements(numbers):
    # Write your code here
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    avg = sum / len(numbers)
    return avg

# to count how many digit in the given list is greater than average value of the list
def count_elements_above_average(numbers):
    # Write your code here
    sum = 0
    count = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    avg = sum / len(numbers)

    for j in range(len(numbers)):
        if numbers[j] > avg:
            count = count + 1
    return count
    pass

# to generate all the possible sublist of a given number in a list
def find_all_sublists(a):
    b = []
    for i in range(len(a)):
        c = []
        for j in range(i, len(a)):

            c.append(a[j])

            b.append(c.copy())
    return b
  
# product of element of a given list
def product_of_list_elements(numbers):
    # Write your code here
    product = 1
    for i in range(len(numbers)):
        product = product * numbers[i]
    return product

    pass
  
# print unique element only
def print_unique_elements(a):
    # Write your code here
    result = []
    for i in range(len(a)):
        for j in range (len(a)):
            if a[i] == a[j] and i!=j:
                break
        else:
            result.append(a[i])
    return result

# merge list's element alternatively from two list one by one

def merge_lists_alternately(list1, list2):
    # Write your code here
    a = []
    for i in range(len(list1)):
        a.append(list1[i])
        for j in range(i,len(list2)):
            a.append(list2[j])
            break
    if len (list2) > len(list1):
        for j in range (len(list1), len(list2)):
            a.append(list2[j])
    
    return a
    pass

