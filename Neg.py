# 33. Python program to print negative numbers in a list

neg = []
list1 = [1,2,3,-1, -2, -3]
for i in list1 :
    if i < 0:
        neg.append(i)
print(neg)