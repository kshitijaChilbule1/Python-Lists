# 28.Python program to print odd numbers in a List

odd = []
list1 = [1,2,3,4,5]
for i in list1:
    if i%2 != 0:
        odd.append(i)
print(odd)