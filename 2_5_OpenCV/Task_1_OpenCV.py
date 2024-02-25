# pip install opencv-python
# Одна из целей OpenCV – предоставить простую для использования инфраструктуру
# компьютерного зрения,
# которая позволила бы быстро создавать относительно сложные приложения.
# Библиотека OpenCV насчитывает
# свыше 500 функций, охватывающих многие области компьютерного зрения,
# в т. ч. контроль качества продукции,
# медицинские изображения, безопасность, пользовательские интерфейсы,
# калибровку камеры, стереозрение и робототехнику.

# Компьютерным зрением называется преобразование данных, полученных от фото
# или видеокамеры,
# результатом которого является некоторое решение или новое представление.
# Преобразование производится ради достижения определенной цели.


import cv2


img = cv2.imread("py.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

edges = cv2.Canny(gray, 50, 150)  # Пороговые значения


cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
# Обнаружение краёв
cv2.imshow("Edges", edges)
cv2.waitKey(10000)
cv2.destroyAllWindows()