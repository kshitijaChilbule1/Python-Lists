# 26. Python program to find second largest number in a list

list1 = [1,2,3,4,5]
maxNum = max(list1)
list1.remove(maxNum)

secondLargest = max(list1)
print(secondLargest)