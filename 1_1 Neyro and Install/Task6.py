# Нахождение глаз
import cv2

# Загрузка каскада для обнаружения лица
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Загрузка каскада для обнаружения лица
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(1) # Создаём объект захвата видео с камеры
while True:
    success, img = cap.read()  # Захват изображения из видеопотока
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Преобразуем изображение в оттенки серого
    # Обнаружение лица на изображении
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x, y, w, h) in faces: # Перебор каждого обнаруженного лица
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Рисование прямоугольника вокруг лица
        img_gray_face = img_gray[y:y + h, x:x + w]  # извлечение области лица в цвете

        # Обнаружение глаз на каждом изображении лица
        eyes = eye_cascade.detectMultiScale(img_gray_face, 1.1, 19)
        # Перебор глаз
        for (ex, ey, ew, eh) in eyes:
            # Рисование прямоугольника вокруг глаз
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), 2)

    cv2.imshow('rez', img) # Отображаем результаты изображения и обработки лица и глаз
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# В заключение следует сказать, что использование OpenCV с нейронной сетью может стать отличным способом
# объединить мощь компьютерного зрения и глубокого обучения.
#
# С помощью правильных инструментов и ресурсов вы можете обучать нейронные сети решать сложные задачи машинного зрения,
# такие как обнаружение объектов, сегментация и классификация. Ключ в том, чтобы понять, как использовать OpenCV
# и выбранную вами среду глубокого обучения для создания, обучения и запуска нейронной сети.
# Это может потребовать крутой кривой обучения, но результаты могут того стоить, поскольку нейронные
# сети оказались очень эффективными для многих задач компьютерного зрения.