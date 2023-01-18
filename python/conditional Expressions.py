# ________________________________________
#
#      CONDITIONAL EXPRESSIONS
# ---------------------------------------

# if else and elif in python
# if else and elif statements are a multiway decision taken by our program due to certain condition in our code

# syntx
'''
if(condition):
    print("yes")
elif(condition2):
    print("no")
else:
    print("maybe")
'''


# program
'''
a=45
if(a<3):
    print("the value of a is greater than 3")
elif(a<7):
    print("the value of a is less than 7")
else:
    print("the value is not greater than 3 or 7")
'''



# create a ladder of  elif
# create diffrent entity,s of IF statements
# else is not complsry




# write a program to print yes the age entered by the user is greater than or equal to 18
'''
a=int(input("enter age ="))
if(a>18):
    print("yes")
else:
    print("sorry age is not greater than 18")
'''




# Relations operators
# relational operators are used to evaluate conditions inside the if statement.
'''==
>=
<=
!=
'''




'''# logical operators
# in python logical operators operate on conditional statements
#     and
a=45
if ((a>34) and (a<56)):
    print("you can work with us")
else:
    print("cant work")

#     or
a=int(input("enter age"))
if ((a>34) or (a<56)):
    print("you can work with us")
else:
    print("cant work")
#     not ''''''revert true to  false and false to true
'''





'''
# in______and____is   how to use in conditional expressions and also it is used in loops
a=None
if(a is None):
    print("yes")
else:
    print("no")
# _______________________

b=[3,4,5,6,7,7,8,7,6,5]
if(3 in b):
    print("yes")
else:
    print("no")
'''



# find the greatest number among the 4 numbers
'''
a=int(input("number="))
b=int(input("number="))
c=int(input("number="))
d=int(input("number="))

if (a>b):
    f1=a
else:
    f1=b
if (c>d):
    f2=c
else:
    f2=d
if(f1>f2):
    print(f1)
else:
    print(f2)
'''




# write a program to find wether a student is pass or fail if it requires 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user
'''
English=int(input("marks="))
Hindi=int(input("marks="))
Marathi=int(input("marks="))
d=((English+Hindi+Marathi)/3)

if (English<33) or (Marathi<33) or (Hindi<33):
    print("you are fail due to insufficient marks")
elif(English+Hindi+Marathi)/3<40:
    print("you are fail due to insufffient Percent")
else:
    print("pappu pass ho gaya")
'''



# A spam comment is defined as a text containinng following keywords;
# make  a lot of money ,buy now,subscribe this,click this,
# write a program to detect this spams
'''
text=input("write a text=")
if "subScribe now " in text:
    print("SPAM")
elif "buy now " in text:
    print("SPAM")
elif "make a lot of money " in text:
    print("SPAM")
elif "click this" in text:
    print("SPAM")
else:
    print("its not a SPAM")
'''