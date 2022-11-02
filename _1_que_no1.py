# 1. write program to find all pairs of integer array whose sum is equal to a given number

list = [6,8,9,4,5,7]

no = 14
pair_array = []

for i in range(len(list)-1):
    for j in range(i + 1,len(list)):
        sum = list[i] + list[j]

        if sum == no:
            pair_array.append([list[i],list[j]])

print(pair_array)