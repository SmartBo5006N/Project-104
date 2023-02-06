import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Mercury", (150,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Venus", (200,220), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Earth", (250,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Mars", (400,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Jupiter", (500,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Saturn", (850,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Uranus", (950,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))
cv2.putText(img, "Neptune", (1050,200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color= (0,255,0))

cv2.imshow("Planets", img)
cv2.waitKey(0)