# 31. Python program to count Even and Odd numbers in a List


evenCount = 0
oddCount = 0
list1 = [1,2,3,4,5,6, 7]
for i in list1:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(evenCount, oddCount)
