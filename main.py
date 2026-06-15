import cv2

#Abrir a camera
camera = cv2.VideoCapture(2)

#Detectar rostos
detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

while True:

    ok, frame = camera.read()

    if not ok:
        break

    cinza = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    rostos = detector.detectMultiScale(
        cinza,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in rostos:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Camera", frame)

    tecla = cv2.waitKey(1)

    #Salvar a foto("s")
    if tecla == ord("s"):
        cv2.imwrite("foto.jpg", frame)
        print("Foto salva!")

    #Fechar a camera(ESC)
    if tecla == 27:
        break

camera.release()
cv2.destroyAllWindows()