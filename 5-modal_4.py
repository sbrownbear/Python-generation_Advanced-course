# 4.2.1
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)


# 4.2.2
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']

list1[2][1][2].extend(['h', 'i', 'j'])

print(list1)


# 4.2.3
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

maximum = -1
for li in list1:
    if max(li) > maximum:
        maximum = max(li)

print(maximum)


# 4.2.4
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

for elem in list1:
    elem.reverse()

print(list1)


# 4.2.5
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0