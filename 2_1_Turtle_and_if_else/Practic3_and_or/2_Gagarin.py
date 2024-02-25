""" 
Первый человек, который отправился в космос 12 апреля 1961 года 
был русский летчик-космонавт Юрий Алексеевич Гагарин,
СССР. Его рост был 157 см, а вес 47 кг. Юрий Гагарин 
и его дублер Герман Титов соответствовали особым габаритам
космонавта, который мог разместиться в кабине пилота. 
Но выбор всё-таки упал на Юрия Алексеевича.
Написать программу, которая могла бы определить 
по введенным данным роста и веса космонавта его возможность
разместиться в космическом корабле 
с ограничением веса от 46 до 51 кг и роста от 156 до 160 см.
Проверьте выполнение задачи по данным Юрия Гагарина

""" #

height = float(input('Введите рост космонавта: '))
weight = float(input('Введите вес космонавта: '))

if 46 <= weight <= 51 and 156 <= height <= 160:
    print('Соответствует требованиям габаритов пилота 1961 года для полёта в космос')
else:
    print('Не соответствует требованиям габаритов пилота 1961 года для полёта в космос')

if height == 157 and weight == 47:
    print("Это габариты летчика-космонавта Юрия Алексеевича Гагарина!")

print('Вы указали рост =', height,'и вес =',weight)
