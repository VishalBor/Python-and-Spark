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