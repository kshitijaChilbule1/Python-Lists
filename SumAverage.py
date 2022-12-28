# 21. Python Program to find sum and average of List in Python

list1  = [1,2,3,4,5]

sum = 0
avg = 0
for i in list1:
    sum += i
    avg = int(sum / len(list1))
print(sum, avg)
