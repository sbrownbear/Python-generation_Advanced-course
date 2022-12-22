# 2.1.1
a, b = int(input()), int(input()) 
print(a+b) #сумма чисел
print(a-b) #разность чисел
print(a*b) #произведение чисел
print(a/b) #частное чисел
print(a//b) #целую часть от деления числа
print(a%b) #остаток от деления числа
print((a**10+b**10)**0.5) #корень квадратный из суммы

# 2.1.2
weight = float(input())
height = float(input())
index_m = float(weight / (height*height)) 

if index_m < 18.5:
    print ("Недостаточная масса")
elif index_m > 25:
    print ("Избыточная масса")
else: print("Оптимальная масса")

# 2.1.3
string = input()
rub = len(string) * 0.6
kop = len(string) * 60 % 100
print(int(rub), 'р.', kop, 'коп.')

# or
res = len(input()) * 60
print(res // 100, 'р.', res % 100, 'коп.')

# 2.1.4
print(len(input().split()))

# 2.1.5
year = int(input())
animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
print(animals[year % 12])

# 2.1.6
s = str(input())
s1 = s[0:-5]
s2 = s[:-6:-1]
s3 = int(s1 + s2)
print(s3)

# 2.1.7
number = input()
number = list(number)
for i in range(len(number) - 3, 0, -3):
    number.insert(i, ',')
print(''.join(number))

# 2.1.8
n, k = int(input()), int(input())
s = [i for i in range (1, n+1)]
while len(s) > 1:
    for q in range (0, k-1):
        s.append(s[q])
    del s[:k]
print(*s)

# or
n = int(input())
k = int(input())
 
res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)