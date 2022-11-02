# 4. write program to print the first non- repeated character from a string



str = input("Enter the string :")
count = 0
dt = {}

for i in range(len(str)):
    if str[i] in dt.keys():
        continue
    for j in range( i + 1, len(str),1):

        if str[i] == str[j]:
            count +=1
    dt[str[i]] = count
    count = 0

for i in dt:
        if dt[i] ==0:
            print("1st non repeated value is :",i)
            break
print(dt)
    
