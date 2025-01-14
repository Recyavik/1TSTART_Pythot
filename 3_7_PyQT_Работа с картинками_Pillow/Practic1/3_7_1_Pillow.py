# Pillow — это библиотека для работы с изображениями в Python,
# которая предоставляет удобный и простой интерфейс для загрузки,
# изменения и сохранения изображений в различных форматах.
# Библиотека Pillow основана на библиотеке PIL (Python Imaging Library).
# Она предоставляет улучшенные возможности по работе
# с изображениями и улучшенную поддержку форматов файлов.
# Pillow имеет широкий спектр функций для работы с изображениями,
# включая изменение размера, обрезку, наложение фильтров,
# преобразование изображений в различные форматы и многое другое.
# Pillow может использоваться для создания графических интерфейсов,
# веб-приложений, обработки изображений в машинном обучении
# и во многих других приложениях, где требуется работа с изображениями.
# pip install Pillow

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PIL import Image

app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 970, 620)

# загружаем изображение с помощью библиотеки Pillow
img = Image.open('img.png')

# создаем объект QPixmap из загруженного изображения
pixmap = QPixmap(img.filename)

# создаем элемент Label
label = QLabel(window)

# устанавливаем изображение в качестве содержимого элемента Label
label.setPixmap(pixmap)

# размещаем элемент Label на форме
label.move(5, 5)

window.show()
app.exec()
