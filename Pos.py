# 32. Python program to print positive numbers in a list

pos = []
list1 = [1,2,3,-1, -2, -3]
for i in list1 :
    if i > 0:
        pos.append(i)
print(pos)
