# _____________________
#     DICTIONARY
# ______________________
# Dictionary is a collection of key_value Pairs
# it is unordered
# it is mutable
# it is indexed
#cannot contains duplicate keys


Dict={
    "vishal":"borkar",
    "pooja":"borkar",
    "om":"shingade",
    "shruti":"shingade",
    "pallavi":"Deokate",
    "marks":[1,2,3],
    "adict":{"key":"value"}
}
print(Dict)
print(Dict["shruti"])
print(Dict["marks"])

# change value
Dict["marks"]=[45,89]
print(Dict)


# DICTIONARY methods
# print only keys
print(Dict.keys())


# Print values of Dict
print(Dict.values())


# items....returs tuple of each key value
print(Dict.items())



# update the dict
a={
    "abc":"123"
}
Dict.update(a)
print(Dict)

print(Dict.get("vishal"))


# _________________________________
#           SETS
# ---------------------------------

# set is a collection of non repetative elements
# sets are unordered
# sets are unindixed
# There is no way to change items in sets
# Sets cannot contain duplicate values

# type of j
'''
j = {1,2,3,5}
print(type(j))
'''

# not contains duplicate
'''
j = {1,2,3,5,5}
print(j)
'''

#the empty set can be created by using following syntax
'''j=set()
print(type(j))
'''

# set methods

# add  ...adds element to set
# we can only add tuples to set
'''
j=set()
j.add(2)
print(j)
print(type(j))
'''

# len.....give length without duplicates
'''
j={1,3,4,5,4,3,2,1}
print(len(j))
'''

# remove.....removes element from set
'''
j={1,3,4,5,4,3,2,1}
j.remove(5)
print(j)
'''

# pop''''removes random value
j={1,3,4,5,4,3,2,1}
j.pop()
print(j)

# clear.....clears the set
j={1,3,4,5,4,3,2,1}
j.clear()
print(j)


'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	        Description
add()	        Adds an element to the set
clear()	        Removes all the elements from the set
copy()	        Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	    Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	    Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	        Removes an element from the set
remove()	    Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	        Return a set containing the union of sets
update()	    Update the set with the union of this set and others
'''