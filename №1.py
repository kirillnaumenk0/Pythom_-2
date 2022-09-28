# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = str(input('Введите число: '))
num_tr = int(float(num) * 10 **(len(num)-2))
summa = 0
for i in range((len(num)**2)-1):
    if (num_tr % 10) != 0:
        summa += (num_tr % 10)
    num_tr //= 10
print(summa)
    
