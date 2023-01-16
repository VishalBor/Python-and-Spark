# list
# create a list usint using []

a=[1,2,3,4,5,6,6,77,7,8]

# access using index and slicing
print(a[0])
print(a[1])
print(a[0:5])
print(a[::-1])

# changing the index of list
a[0]=5
print(a)

# we can create a list items of diffrent types
c=[45,"vishal",True,False]


# slicing
friends=["vishal","pooja","akash","ajay","amol"]
print(friends[0:3])


# List Methods
l1=[2,1,2,3,4,5,6,7,7,8,8,9,9,9]

# sort
l1.sort()
print(l1)

# reverse
l1.reverse()
print(l1)

# appernd
l1.append(45)
print(l1)

# insert
l1.insert(0,0)
l1.insert(3,5)
print(l1)

# pop   removes last element
# l1.pop()
# print(l1)

# remove  .removes selected element from list
l1.remove(1)
print(l1)