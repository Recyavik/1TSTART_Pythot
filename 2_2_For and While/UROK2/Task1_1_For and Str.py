# ЦИКЛ for (алгоритмическая структура перебора последовательности)
# Задача 1. Перебор символов в строке

liters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
for liter in liters:
    # print(liter, end=',')
    i = i + 1
    print(i, "- символ = ", liter)

print()
for i in range(len(liters)):
    print(i+1, "- символ = ", liters[i])

print()
for i in range(0, len(liters), 3):
    print(i+1, "- символ = ", liters[i])

for chr in 'aabb7ccc': # параметр chr посимвольно пройдет по всей строке
    if chr.isdigit(): # если в одном из символов строки появится цифра,
        break # то цикл прервется
    print(chr, end='')

for i in range(1, 10): # запуск вывода чисел от 1 до 10 не включительно
    if i % 3 == 0: # если параметр цикла будет кратен 3 (такие числа как 3,6,9)
        continue # то этот параметр будет пропущен и цикл перейдет на следующий шаг
    print(i,end=' ')

# Сегодня на практике - ЦИКЛ for (алгоритмическая структура перебора последовательности)
# Задача 2. Перебор чисел последовательности
import random as rnd
import math


for x in range(1, 15, 1):
    if x % 2 == 0:
        print(x, end=' ')

print()
for x in range(2, 15, 2):
    print(x, end=' ')

print()

for i in range(0, 5):
    a = rnd.randint(10, 99)
    x = math.sqrt(a)
    print(a, "его корень квадратный =", x)

### Рассмотрим задачу с использованием остановки break и пропуска итерации continue.
# Например: Пользователь вводит 10 натуральных чисел (например 10 монет, которые он бросает в копилку), а программа будет находить значение суммы этих чисел.
# Если сумма всех введенных чисел превысит 100, то нужно прервать цикл и вывести накопленную сумму.
# Также необходимо учитывать, что не всякий пользователь знает какие числа натуральные и может вводить отрицательные числа, которые суммированию не подлежат.
summa = 0 # инициализация суммы
for iteration in range(1,10+1): # запуск 10 повторов с 1 по 10 включительно
    x = int(input('Введите натуральное число: ')) #ввод натурального числа
    if x <= 0:  # условие для пропуска отрицательных чисел и равных 0
        continue # пропуск итерации, если условие ИСТИНА, т.е. x<=0
    summa = summa + x # нахождение суммы
    print('Сумма = ',summa) # вывод промежуточного результата суммы
    if summa >= 100: # условие преждевременного прерывания цикла
        break   # прерывание цикла, если условие ИСТИНА, т.е. Сумма >=100
print(summa)

# Добавив к условию задачи маркер else: можно сообщить, что количество чисел (монет) более 10 недопустимо.
summa = 0 # инициализация суммы
for iteration in range(1,10+1): # запуск 10 повторов с 1 по 10 включительно
    x = int(input('Введите '+str(iteration)+'-ое натуральное число: ')) #ввод натурального числа
    if x <= 0:  # условие для пропуска отрицательных чисел и равных 0
        continue # пропуск итерации, если условие ИСТИНА, т.е. x<=0
    summa = summa + x # нахождение суммы
    print('Сумма = ',summa) # вывод промежуточного результата суммы
    if summa >= 100: # условие преждевременного прерывания цикла
        break   # прерывание цикла, если условие ИСТИНА, т.е. Сумма >=100
else: # используется при условии, что цикл прошел все свои итерации.
    print('Вы ввели 10 числовых значений, суммирование в цикле завершено ')
print('Итоговая сумма =', summa)