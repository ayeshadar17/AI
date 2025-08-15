import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C://Users//HP//Downloads//AIEPCM2L2_Activities_Boilerplate_code_(2)-7a3e//AIEPCM2L2 Activities Boilerplate code//example.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("GGB Image")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()