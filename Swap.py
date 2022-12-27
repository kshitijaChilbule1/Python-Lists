# 2. Python program to swap two elements in a list

list1 = [1,2,3,4,5]
temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)