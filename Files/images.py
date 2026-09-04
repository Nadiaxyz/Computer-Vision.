import cv2

image = cv2.imread("../Images/piano (1).png")

cv2.imshow("Shirt Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
