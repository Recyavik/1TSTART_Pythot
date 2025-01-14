# Атрибут экземпляра класса – это переменная, определенная внутри класса и
# принадлежащая каждому отдельному объекту (экземпляру) этого класса.
# Они используются для хранения информации, которая является уникальной для каждого объекта.
# Атрибуты экземпляра инициализируются в методе `__init__()`
# и могут быть использованы или изменены только через объекты класса.

class Citizen: # Гражданин
    subject = "Гражданин"

# Конструктор класса — это специальный метод, который автоматически вызывается
# при создании нового объекта (экземпляра) класса.
# В Python, конструктор класса имеет имя `__init__` и является встроенным методом для инициализации объекта.
# Основная задача конструктора — инициализация данных объекта и выполнение необходимых
# действий для подготовки объекта к использованию. Конструктор обычно принимает аргументы,
# которые определяют начальные значения атрибутов объекта.

    def __init__(self, name='Неизвестное', age=None):
        self.name = name
        self.age = age

    def say(self, message):
        print(self.name, ": говорит - ", message)

    def sing(self):
        print(self.name, ": поёт")

    def go(self, speed):
        print(self.name, "идёт со скоростью: ", speed, "км/ч")
        if speed < 3:
            self.sing()

# Атрибуты экземпляра можно использовать для доступа, изменения их значений и передачи их
# значениям других функций или методов. Атрибуты экземпляра доступны только через объекты класса.
alex = Citizen("Алексей", 30)
alex.name = 'Лёха'
alex.age = 31
# Экземпляр класса теперь знает свой name и age
# (своё имя и возраст, которые принадлежат только этому экземпляру класса)

# Передадим методу go экземпляра класса alex атрибут 4 и вызовем этот метод
alex.go(4)
alex.go(2)

alex.say("Что еще вам спеть ?")

sasha = Citizen("Саша", 18)
# Теперь экземпляр класса тоже знает свой name и age
# (своё имя и возраст, которые принадлежат только этому экземпляру класса)
print(sasha.name, sasha.age)
# Причём мы можем обращаться и изменять атрибуты класса не только в момент инициализации,
# а в любой момент имеем доступ к атрибутам через точку
sasha.name = "Александр"
print(sasha.name)
sasha.age = sasha.age + 1
print(f"Сегодня {sasha.name} празднует свой {sasha.age} день рождения!")
# Таким образом, атрибуты экземпляра класса используются для хранения уникальных значений,
# связанных с каждым объектом класса, и могут быть использованы
# в методах класса для реализации различных функций и поведения.
w = Citizen()
print(w.name, w.age)

