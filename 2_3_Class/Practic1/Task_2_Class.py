# Объявление класса с помощью ключевого слова "class" является стандартным способом
# создания класса в объектно-ориентированных языках программирования.

class Person:
    subject = "Человек" # Является атрибутом класса
# При изменении значения атрибута класса, он изменяется у всех объектов класса,
# так как атрибут класса разделяет свое значение между всеми объектами.
# Важно отметить, что атрибуты класса следует использовать с осторожностью
# и только для хранения значений, общих для всех объектов класса.
# В противном случае лучше использовать атрибуты экземпляра, которые уникальны для каждого объекта.

    def sing(self):     # Является методом экземпляра класса
# Здесь «self» – это ссылка на экземпляр класса,
# она используется для доступа к атрибутам и методам объекта внутри самого класса.
        print("Пою")
    def say(self, message):
    # say Является методом класса с параметром message, т.е. атрибутом экземпляра класса в методе say
        print("Говорю: ", message)

    def go(self, speed):
    # go Является методом класса с параметром speed, т.е. атрибутом экземпляра класса в методе say
        print("Иду со скоростью: ", speed, "км/ч")
        # Не забыть в конце
        self.sing() # Методы могут обладать функционалом вызова других методов этого же класса

# Создадим экземпляр класса
oleg = Person()
# Передадим в метод экземпляра класса атрибут message
oleg.say("Привет, я - Олег!")
# Можем обратиться к атрибуту класса, который принадлежит всем экземплярам класса
print("Я -", oleg.subject)

# Создадим ещё 2 экземпляра класса
nina = Person()
tanya = Person()
#  они получат функционал описанный внутри класса Person
tanya.say("Привет! Я - Таня!")
print("Я -", tanya.subject)
nina.say("Привет! Я - Нина!")
print("Я -", nina.subject)

# Пусть экземпляры класса поговорят
nina.say("Здравствуй!")
tanya.say("Как дела?")
nina.say("Спасибо нормально!")
nina.go(5) # Обращение к методу экземпляра класса позволяет вызвать метод экземпляра класса,
# описанный внутри класса

# Таким образом, при помощи классов мы можем создавать и управлять объектами
# в объектно-ориентированном программировании. Это позволяет повысить модульность,
# масштабируемость и управляемость кода.