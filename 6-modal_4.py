# 4.3.1
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n+1)))
    
print(*result, sep='\n')


# 4.3.2

n = int(input())
result = []

for i in range(1, n+1):
    result.append(list(range(1, i+1)))
    
print(*result, sep='\n')


# 4.3.3

n = int(input())
lst = [[1]]
for i in range(1, n+1):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = lst[i-1][j-1] + lst[i - 1][j]
    lst.append(row)

print(lst[-1])


# 4.3.4

n = int(input())
lst = []
for i in range(n):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = lst[i-1][j-1] + lst[i - 1][j]
    lst.append(row)
for x in lst:
    print(*x)