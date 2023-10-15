#Задание 1
a = int(input('Введите число: '))
if a / 1 <= 0:
    print('Не является простым')
elif a / 2 <= 0:
    print('Не является простым')
elif a <= 0:
    print('Не является простым')
else:
    print('Является простым')



#Задание 2
n = 6
mas = [9,6,-0.6,2,8,14]
for run in range(n-1):
    for i in range(n-1):
        if mas[i]>mas[i+1]:
            mas[i],mas[i+1] = mas[i+1],mas[i]
print(*mas)



#Задание 3
a = [9,6,-0.6,2,8,14]
print(max(a))



#Задание 4
f1 = 1
f2 = 2
n =int(input(':'))
print(f1, f2, end=' ')
while f2 < n:
    print(f2, end=' ')
    f1, f2 = f2, f1 + f2
