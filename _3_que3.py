# 3. write a program to check if two strings are a rotation of each other?

str1= input("Enter the str1:")
str2 = input("Enter the str2:")

if len(str1) == len(str2):
    temp = str1 + str2
    if str2 in temp:
        print("rotation")

else:
        print("no rotation")

