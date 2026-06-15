import cv2

detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

print(detector.empty())