import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
"Sun",
(100,80),
cv2.FONT_HERSHEY_COMPLEX,
2,
(0,0,255))

cv2.putText(img,
"Mercury",
(90,250),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(0,0,255))

cv2.putText(img,
"Venus",
(180,260),
cv2.FONT_HERSHEY_COMPLEX,
0.8,
(0,0,255))

cv2.putText(img,
"Earth",
(280,260),
cv2.FONT_HERSHEY_COMPLEX,
0.8,
(0,0,255))

cv2.putText(img,
"Moon",
(320,160),
cv2.FONT_HERSHEY_COMPLEX,
0.6,
(0,0,255))

cv2.putText(img,
"Mars",
(370,260),
cv2.FONT_HERSHEY_COMPLEX,
0.8,
(0,0,255))

cv2.putText(img,
"Jupiter",
(480,400),
cv2.FONT_HERSHEY_COMPLEX,
2,
(0,0,255))

cv2.putText(img,
"Saturn",
(750,350),
cv2.FONT_HERSHEY_COMPLEX,
1,
(0,0,255))

cv2.putText(img,
"Neptune",
(940,300),
cv2.FONT_HERSHEY_COMPLEX,
1,
(0,0,255))

cv2.putText(img,
"Uranus",
(1110,300),
cv2.FONT_HERSHEY_COMPLEX,
1,
(0,0,255))

cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.imshow("Output", img)
cv2.waitKey(0)