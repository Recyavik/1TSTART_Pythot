# Оператор with в Python предназначен для облегчения работы с ресурсами,
# которые требуют корректного освобождения после использования.
# Частыми примерами таких ресурсов являются файлы или сетевые соединения.

# Добавление
# В контексте работы с файлами и данными существует несколько способов записи: добавление,
# перезапись и запись множества строк. Мы рассмотрим каждый из них, чтобы лучше понять, как они работают:


# Добавление информации в файл подразумевает добавление новых данных в конец файла, не затрагивая существующие данные.
# Например, если у вас есть файл с текстом «Привет, мир!», и вы хотите добавить фразу « Как дела?»,
# результатом будет файл с текстом «Привет, мир! Как дела?».
# В Python для добавления данных в файл используется режим "a" при открытии файла. Например:
with open('file.txt', 'a') as f:
    f.write(" Как дела?")

# Перезапись данных в файле означает удаление существующих данных и замена их новыми.
# Например, если у вас есть файл с текстом «Привет, мир!», и вы хотите перезаписать его с фразой «Как дела?»,
# в файле будет только новый текст «Как дела?».
#
# В Python для перезаписи данных в файле используется режим "w" при открытии файла:
# Перезапись
with open('file.txt', 'w') as f:
    f.write("Как дела?")


# Запись множества строк в файле – это режим записи, при котором вы можете записать несколько строк
# в файл за одну операцию. Это может быть полезно, например, при записи списков данных или таблиц.
# В Python запись множества строк может быть выполнена с помощью функции writelines():
# Запись множества строк
with open('file.txt', 'w') as f:
    lines = ["Привет, мир!\n", "Как дела?\n"]
    f.writelines(lines)
# Здесь мы записываем список строк `lines` в файл file.txt. В результате файл будет содержать две строки текста:
# Привет, мир!
# Как дела?


# Запись списка или других форматов данных в файл включает преобразование данных в строковый формат
# и последующую запись этих строк в файл. Я ниже объясню примеры записи списков и словарей в файлы, используя Python.
# Запись списка
numbers = [1, 2, 3, 4, 5]
# Чтобы записать этот список в файл, вам нужно будет преобразовать каждое число в строковый формат и разделить их,
# например, с помощью символов новой строки, чтобы каждое число было на отдельной строке:
with open('numbers.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + "\n")


# Предположим, у нас есть следующий словарь, который мы хотим записать в файл:
# Запись словаря
# Для записи словаря в файл, вы можете преобразовать каждую пару ключ-значение в строку и записать
# их на отдельных строках.
# Например:
data = {"name": "Alice", "age": 30, "city": "New York"}
with open('data.txt', 'w') as f:
    for key, value in data.items():
        f.write(f"{key}: {value}\n")


