# write a program to reverse a string
# Method 1
'''
def reverse(string):
    string=string[::-1]
    return string

a=input("enter a string to reversee it=")
print(reverse(a))
'''

# Method 2
'''def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]

a="vishal"
print(reverse(a))'''


# write a program to reverse a numbers
'''
num = 123456789
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
'''


