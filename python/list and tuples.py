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

# pop removes last element
# l1.pop()
# l1.pop(2)
# print(l1)

# remove  .removes selected element from list
l1.remove(1)
print(l1)

# count ...counts the given element element
print(l1.count(45))

# clear   ...clers the list
# print(l1.clear())

# join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# using for loop join 2 lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    print(list1)


#copy list
list1 = ["a", "b", "c"]
mylist=list1.copy()
print(mylist)
