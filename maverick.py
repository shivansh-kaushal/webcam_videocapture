import cv2
frameWidth = 640
frameHeight = 360
cap = cv2.VideoCapture("E:\/check.mp4")
cap.set(3,frameWidth)
cap.set(4,frameHeight)
while True:
    sucess,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break