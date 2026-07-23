# concept of indexing
a = 'nature'
print (a)
print(a[4])
print(a[:6])
print(a[-1])

# concept of negative indexing
# - ve 1 is tagged to the last of given word and so on
print (a[-3])

# string slicing
# there is concept of start, stop, and step
# format
print(a[:6:2])
# here the first number shows start, 2nd says about stop and third says about step
str1 = " hello i am a data scientist"
# extract heloo data and scientist from above string
print(str1[0:6:1] , str1 [13:17:1], str1 [18:27:1])

# string object does not suppport item assignment

