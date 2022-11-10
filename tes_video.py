import cv2

img = cv2.imread("photos\gatinho-shrek.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)

cv2.imshow("Image", img)
cv2.imshow("blur Image", imgGray)
cv2.imshow("canny Image", imgCanny)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# cap.set(3,640)
# cap.set(4,480)
# cap.set(10, 100)


# while True:
#     succes, img = cap.read()
#     cv2.imshow("Video", img)
#     if  cv2.waitKey(1) & 0xFF == ord('q'):
#         break

