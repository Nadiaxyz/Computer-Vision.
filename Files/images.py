import cv2
import os

image_path = os.path.join(os.path.dirname(__file__), "..", "Images", "piano (1).png")

image = cv2.imread(image_path)

if image is None:
    print("Image could not be loaded!")
else:
    cv2.imshow("Piano Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
