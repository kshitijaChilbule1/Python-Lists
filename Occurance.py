# 20. Python | Count occurrences of an element in a list

list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10, 10]

x = 10
count = 0

for i in list1:
    if i == x:
        count += 1
print(count)
