# Конструктор класса — это специальный метод, который автоматически вызывается
# при создании нового объекта (экземпляра) класса.

# В Python конструкторы определены с помощью специальных методов __init__ и __new__.
# Они играют важную роль в объектно-ориентированном программировании, определяя, как создаются объекты класса.
# Поскольку __new__ отвечает за создание объекта, а __init__ — за его инициализацию,
# их часто используют вместе. Особенно это полезно,
# когда ваши объекты требуют некоторого сложного процесса инициализации.

# В Python, конструктор класса имеет
# имя `__init__` и является встроенным методом для инициализации объекта.
# Основная задача конструктора — инициализация данных объекта и выполнение необходимых
# действий для подготовки объекта к использованию. Конструктор обычно принимает аргументы,
# которые определяют начальные значения атрибутов объекта.

class Rectangle:

    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)

# Смотрите, здесь записан метод __new__, у которого первым идет обязательный параметр cls 
# – это ссылка на текущий класс Point, а затем, указываются коллекции из фактических и формальных параметров, 
# которые может принимать данная функция. Это стандартное определение метода __new__ в классах.
    def __init__(self, width=40, height=30):
        print("Hello from __init__")
        self.width = width
        self.height = height
# Создание объекта: на этом этапе Python вызывает специальный метод __new__,
    # который отвечает за создание нового объекта. Это единственный метод,
    # который может возвращать новый объект класса.
# Инициализация объекта: после создания объекта Python вызывает метод __init__,
    # чтобы инициализировать новый объект. Метод __init__ не возвращает ничего, о
    # н просто устанавливает значения атрибутов объекта.

    def area(self):
        return self.width * self.height


rect1 = Rectangle(10, 20)
print(rect1.width)
print(rect1.height)
print(rect1.area())

rect2 = Rectangle()
print(rect2.width)
print(rect2.height)
print(rect2.area())
