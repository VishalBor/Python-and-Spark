# _______________________________________
#              LISTS
# ______________________________________
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


# _____________________________________________
#
#                 TUPLES
# ______________________________________________

# tuples are immutable data type
# cant update cant change or mannuplated

#empty tuple   a=()

# creating a tuple
b=(1,2,4,5,6,7,8,9)
print(b)
print(b[0])
print(b[1])
print(b[0:5])
print(b[::-1])


# METHODS

# count ...returns no of  apperences
print(b.count(4))

# index
print(b.index(5))
print(b.index(7))

# len ....gives length
print(len(b))

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



# ___________________________________________________
#      QUESTION ON LIST AND TUPLES
# ___________________________________________________


# Write a program to store 7 fruits in a list entered by a user
e=input("enter fruit 1")
f=input("enter fruit 2")
g=input("enter fruit 3")
h=input("enter fruit 4")
i=input("enter fruit 5")
j=input("enter fruit 6")
k=input("enter fruit 7")
list4=[e,f,g,h,i,j,k]
print(list4)

