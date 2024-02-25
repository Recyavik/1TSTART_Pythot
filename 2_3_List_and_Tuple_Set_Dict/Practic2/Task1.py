# Базовые навыки обработки строк
val1 = 16
val2 = 14
print(val1 + val2)

# Конкатенация строк
st1 = "16"
st2 = "14"
print(st1 + st2)

# Дублирование строки
w = 'apple'
print(w * 3)

# Screenshot 1
# Нахождения длины строки, т.е. количество символов в строке можно посчитать функцией len(stroka):
w = 'apple'
d = len(w)
print('Длина "строки"', w,'=', d)

w = 'apple'
print(w[0])
print(w[1])
print(w[len(w) -1])

# Screenshot 2
# У отрицательного индекса строк нумерация идет с конца строки и начинается с -1 у последнего символа:
w = 'cherry'
print(w[-1])
print(w[-2])

print(w[-len(w)])

# Screenshot 3
# Срез строки
w = 'projects'
print(w[3:6])
print(w[2:-2])
print(w[:4])
print(w[1:])
print(w[:])

# Срез строки с шагом извлечения
w = 'projects'
print(w[::-1])
print(w[7:2:-1])
print(w[2::3])

# Методы строк
st = 'Программирование строк на Python' # Исходная строка
d = len(st) # Определим длину строки
print(d)

subst = 'мир' # Подстрока для поиска
pos = st.find(subst, 0, d) # Ищет позицию первого вхождения подстроки в строке с 0 до последнего символа
print(pos)
pos = st.index(subst)
# Аналогичные команды поиска, однако ВАЖНО УЧЕСТЬ, что при отсутствии подстроки в строке программа
# выдаст ошибку (ValueError).
# Если вы не помните как обрабатывать ошибки,
# то советую лучше использовать find или вы должны быть уверены, что поиск будет удачным.

# Поиск подстроки в строке
st = 'Программирование строк на Python' # Исходная строка
subst = 'мир' # Подстрока для поиска
flag = subst in st
print(flag)
subst = 'нота' # Подстрока для поиска
flag = subst in st
print(flag)

# Поиск количества вхождений
st = '10111110101' # Исходная строка
# Функция посчитает количество вхождений подстроки '0' в строке st
count = st.count('0') # Функция
print(count)
# Функция посчитает количество вхождений подстроки '1' в строке st, начиная с st[2]
count = st.count('1', 2) # Функция
print(count)
# Функция посчитает количество вхождений подстроки '1' в строке st,
# начиная с st[2] не включая 3 последних символа (т.е. - 3 символа)
count = st.count('1', 2,-3) # Функция
print(count)

# Замена части строки
st = 'Как слышно?  раз-раз-раз!' # Исходная строка
print(st)
new_st = st.replace('раз', 'два', 2) # Замена по шаблону не более 2
print(new_st)

st = '--Мама-мыла-раму--' # Исходная строка
st3 = st.strip('-') # Функция удаления пробельных символов справа и слева строки
print(st3)

# list = st.split(symbol) Разделяет строку на элементы списка по разделителю.
#st - строка поиска (в этой строке ищем символ разделитель).
#list1-список элементов, который получается в результате разделения строки.
#symbol-это символ, которые определяет признак деления строки.
st = 'Как слышно?  раз-два-три!' # Исходная строка
list1 = st.split('-')
print(list1)

#   st.join(scroll) Соединение элементов списка в единую строку через разделитель
scroll = ['apple', 'banana', 'cherry'] # Список
st = '-' # Разделитель (обычно равен пробелу' ').
newst = st.join(scroll) # Соединение элементов списка в единую строку
print(newst)


# Функции преобразования строк
st = 'avrora' # исходная строка
print(st) # вывод исходной строки на экран

# Функция перевода первого символа строки в верхний регистр st.capitalize()
# Строка не поменяет своё значение, т.к. в Python значения строк не меняется
# st.capitalize() # Не рабочий метод  (хотя записан без ошибок)
print(st) # Вывод строки

# Строку можно изменить только присваиванием
st = st.capitalize() # Рабочий метод
print(st) # Вывод измененной строки

#   st.upper() Преобразование строки в верхний регистр
st = 'байкал'
print(st)
# Преобразование этой строки в верхний регистр
st = st.upper()
print(st)

#   st.lower() Преобразование строки в нижний регистр
# Исходная строка
st = 'ОЗЕРО'
print(st)
# Преобразование этой строки в верхний регистр
st = st.lower()
print(st)

#   st.title() Функция перевода первой буквы с нижнего регистра в верхний
# st - исходная строка
st = 'россия' # Исходная строка
new_st = st.title() # Функция регистра первого символа
print(new_st)

# Методы проверки строк по признаку
#   flag = st.isdigit() Проверка строки на использовании в ней только цифр
# flag = True (ИСТИНА), если строка st состоит только из цифр, а иначе flag = False (ЛОЖЬ)
st = '123 - проверка!'
flag = st.isdigit()
print(flag)
st = '123'
flag = st.isdigit()
print(flag)

# flag = st.startswith(pattern) Проверка строки на использовании в начале строки шаблона подстроки
# flag = True (ИСТИНА), если начало строки st совпадает с шаблоном  pattern
st = 'ПРОГУЛКА' # Исходная строка
pattern = 'ГУЛ' # Шаблон
flag = st.startswith(pattern) # Поиск шаблона в начале исходной строки True/False
print(flag)
st = 'ПРОГУЛ' # Исходная строка
pattern = 'ПРОГУЛ' # Шаблон
flag = st.startswith(pattern) # Поиск шаблона в начале исходной строки True/False
print(flag)