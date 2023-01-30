# __________________________________
#         Python Loops
# __________________________________

# Python has two primitive loop commands:
             # while loops
             # for loops

# With the while loop we can execute a set of statements as long as a condition is true.

# Example
# Print i as long as i is less than 6:
'''
i = 1
while i<6:
    print(i)
    i+=1
'''



# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
'''
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
'''




# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''




# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Example
# Print a message once the condition is false:
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''




# loops make it easy for a programmer to  tell the computer which set of instructions to repeat and how
# there are two types of loop
# while and for

# using while loop print 0 to  9
i=0
while i<10:
    print("yes",i)
    i=i+1
    print("DONE")


# in while loops the conndition is  checked first .if it evalutes to true the body of the loops is executed ,otherwise not.
# if the loop is entered ,the process of  condition check and execuation is continued until the condition becomes false.



# write a program to priint 1 to 50
i=1
while i<=50:
    print(i)
    i=i+1





# write a program to print the conntent of a list usinng while loops
i=0
list=["banana","kiwi","apple","pineapple","jackfruit"]
while i<len(list):
    print(list[i])
    i=i+1



# for loop
# a loop is used to iterate through a sequence like list,tuple,or string


# print list with the help of for loop
list=["banana","kiwi","apple","pineapple","jackfruit"]
for item in list:
    print(item)



# Range function in python
# range(start,stop,step_size)
# the range function in python is used to generate a sequence of numbers...we can also specify the start  ,stop and step size as follows
for b in range(2,8):
    print(b)


# for with else and range

for i in range(10):
    print(i)
else:
    print("this is inside else of for")




# THE BREAK statement
# break is used to come out of the loop when encountered .It instructs  the proggram to Exit the loop  now
for i in range(10):
    print(i)
    if i==5:
        break



# THE CONTINUE STATEMENT
# CONTINUE is used to stop the current iteration of the loop and contine with  the next one  it instructs  the program to skip this iteration:

for i in range(10):
    if i==5:
        continue
    print(i)




# write a program to print multiplication table table of a given number using for loop
num=int(input("enter number"))
for i in range(1,11):
    print(i*num)




# write a program to print multiplication table table of a given number using for loop









# write a program to greet all person names stored in a list and which starts with s
l1=["vishal","pooja","shubham","sachin","sushil"]

for name in l1:
    if name.startswith("s"):
        print("hello" + name)




# Write a program to find wheather a given number is  prie or not
num = int(input("Enter the number"))
prime = True
for i in range(2,num):
    if(num%i==0):
        prime:False
        break
if prime:
    print("this no is prime")
else:
    print("this number is not prime")



# write a program to prit the  following star pattern
# *
# **
# ***
# ****

for i in range(4):
    print("*" * (i+1))

# write a program to print the following star pattern n=2
#        *
#       **
#      ***
#      ****
n=3
for i in range(3):
    print("" * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print("" * (n-i-1))