# Создадим класс построения многоугольника с помощью черепахи и разберем таких два понятия как self и cls
# Мы будем обращаться к методам через объекты класса и непосредственно через сам класс.
import turtle


class Polygon:
    x0 = 0
    y0 = 0
    corners_default = 3
    size_default = 5
    color_default = "black"

    def __init__(self, x=x0, y=y0, corners=corners_default, side=size_default, color=color_default):
        self.x = x

# Self — это ссылка на текущий экземпляр класса.
# Это способ обращения к атрибутам и методам класса изнутри самого класса.
# # В примере выше, self.x = x устанавливает атрибут координаты текущего объекта класса Polygon в значение x,
# переданное в __init__.
# Следует отметить, что self не передается при создании нового объекта класса.
# Python автоматически передает ссылку на текущий объект в self.
        self.y = y
        self.corners = corners
        self.side = side
        self.color = color

    # Метод класса – это функция, определенная внутри класса, которая принимает класс
    # (а не экземпляр класса) в качестве первого аргумента.
    # Методы класса используются для определения функциональности, которая связана с самим классом,
    # а не с его объектами (экземплярами).

    # Чтобы определить метод класса, необходимо использовать декоратор `@classmethod`
    # перед определением метода. Ключевое слово `cls`
    # является общепринятым именем первого параметра метода класса, который ссылается на сам класс.
    @classmethod
    def info_default(cls):
        print(f"Координаты: ({cls.x0},{cls.y0})")
        print(f"Количество углов полигона: {cls.corners_default}")
        print(f"Размер(сторона) полигона: {cls.size_default}")
        print(f"Цвет полигона: {cls.color_default}")

    def draw(self):
        if self.corners < 3 or self.side < 3:
            print("Нельзя построить полигон по этим параметрам")
        else:
            t.pencolor(self.color)
            t.penup()
            t.goto(self.x, self.y)
            t.pendown()
            for _ in range(0, self.corners):
                t.fd(self.side)
                t.right(360/self.corners)


t = turtle.Turtle()
t.pensize(5)
t.speed(0)
t.screen.screensize(400, 400)

triangle = Polygon()
triangle.side = 100
triangle.draw()

square = Polygon(x=200, y=200, color="blue", corners=4, side=80)
square.draw()

polygon_8 = Polygon(-200, 200, 8, 60, "red")
polygon_8.draw()


# Методы класса можно вызывать через имя класса или через объекты (экземпляры) класса.
print("\x1b[92m Доступ к методу через имя класса \x1b[0m")
Polygon.info_default()
print("\x1b[93m Доступ к методу через экземпляры класса \x1b[0m")
polygon_8.info_default()
# В общем, использование классов делает ваш код более структурированным,
# повторно используемым и гибким, что облегчает разработку, отладку и поддержку вашей программы
# - Методы класса логически связаны со всем классом, а не с его экземплярами.
# - Методы класса могут быть унаследованы и переопределены в подклассах,
# что позволяет изменять их поведение для различных классов.
# - Методы класса выполняются на уровне класса, а не на уровне объекта.
# Это означает, что они не требуют инициализации экземпляра класса,
# и независимо от состояния класса возвращает одну и ту же сущность.

# И еще один момент. Когда вы обращаетесь к атрибутам самого класса через экземпляр класса,
# используйте ключевое слово __class__  чтобы случайно не создать атрибут экземпляра класса и не потеряться в данных
print(polygon_8.__class__.color_default)

turtle.done()