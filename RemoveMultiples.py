# 37. Remove multiple elements from a list in Python

# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

list1 = [12, 15, 3, 10]

for i in list1:
    if i == 12 or i == 3:
        list1.remove(i)
print(list1)