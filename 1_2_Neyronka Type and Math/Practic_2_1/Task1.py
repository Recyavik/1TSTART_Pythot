# Напишите программу, которая считывает строку-разделитель и три строки,
# а затем выводит указанные строки через разделитель.

a = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=a)
# 1***2***3

# Сумма трёх чисел
# Напишите программу, которая считывает три целых числа
# и выводит на экран их сумму. Каждое число записано в отдельной строке.
a = int(input())
a += int(input())
a += int(input())
print(a)

# Следующее и предыдущее
# Напишите программу, которая считывает целое число, после чего на экран
# выводится следующее и предыдущее целое число с пояснительным текстом.
a = int(input())
print('Следующее за числом', a, 'число:', a+1)
print('Для числа', a, 'предыдущее число:', a-1)

# Разделяй и властвуй
# Напишите программу, которая считывает целое положительное
# число xx и выводит на экран последовательность
# чисел x, 2x, 3x, 4x, 5x, разделённых тремя черточками.
a = int(input())
print(a, a*2, a*3, a*4, a*5, sep='-'*3)

# Расстояние в метрах
# Напишите программу, которая находит полное число метров по заданному
# числу сантиметров.
a = int(input())
print(a//100)

# Сама неотвратимость
# Безумный титан Танос собрал все 6 камней бесконечности
# и намеревается уничтожить половину населения Вселенной по щелчку пальцев.
# При этом если население Вселенной является нечетным числом,
# то титан проявит милосердие и округлит количество выживших в большую сторону.
# Помогите Мстителям подсчитать количество выживших.
a = int(input())
print(a // 2 + a % 2)

# Пересчет временного интервала
# Напишите программу для пересчёта величины временного интервала,
# заданного в минутах, в величину, выраженную в часах и минутах.
a = int(input())
print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')

# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр
# положительного трёхзначного числа.
a = int(input())
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10
print('Сумма цифр =', a1 + a2 + a3)
print('Произведение цифр =', a1 * a2 * a3)

# Напишите программу для нахождения цифр четырёхзначного числа.
a = int(input())
print("Цифра в позиции тысяч равна", a // 1000)
print("Цифра в позиции сотен равна", a % 1000 // 100)
print("Цифра в позиции десятков равна", a % 100 // 10)
print("Цифра в позиции единиц равна", a % 10)

# Даны два действительных числа a и b. Вычислите их сумму, разность,
# произведение и частное при a=3.79 и b=84.93.



first_name = input("Введите имя: ")
surname = input("Введите фамилию: ")
print("Привет ", first_name, surname)
number = input("Введите номер телефона: ")


a = int(input("Введите сторону a"))
b = int(input("Введите сторону b"))
c = int(input("Введите сторону c"))
p = (a +  b +  c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
print("Площадь треугольника")

# Найти площадь прямоугольника