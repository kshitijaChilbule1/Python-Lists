# 19. Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[2][0])
# print(list1[2][1])
# print(list1[2][1][0])
# print(list1[2][1][1])
list1[2][1][2].extend(sub_list)
print(list1)
# print(list1[2][1][3])
# print(list1[2][2])
# print(list1[3])
# print(list1[4])

