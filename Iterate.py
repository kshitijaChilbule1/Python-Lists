# 14. Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

rev_list2 = list2[::-1]
print(rev_list2)

list3 = [(i, j) for i, j in zip(list1, rev_list2)]
print(list3)