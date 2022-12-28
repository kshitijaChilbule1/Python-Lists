# 36.Python program to count positive and negative numbers in a list

pos = 0
neg = 0
list1 = [1,2,3,4,5,-1,-2,-3,-4,-5]
for i in list1:
    if i > 0:
        pos += 1
    else:
        neg += 1

print(pos, neg)
