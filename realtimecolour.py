import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply the selecte color filter or edge detection."""
    filtered_image = image.copy()

    if filter_type =="red_tint":
        filtered_image[:, :, 1] = 0 # Green channel to 0
        filtered_image[:, :, 0] = 0
    elif filter_type =="green_tint":
        filtered_image[:, :, 0] = 0 # Green channel to 0
        filtered_image[:, :, 2] = 0     
    elif filter_type =="blue_tingt":
        filtered_image[:, :, 1] = 0 # Green channel to 0
        filtered_image[:, :, 2] = 0 
    elif filter_type =="sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.sobel(gray_image, cv2.CV_6F, 1, 0, ksize=3)      
        sobely = cv2.sobel(gray_image, cv2.CV_6F, 0, 1, ksize=3)  
        combined_sobel = cv2.bitwise_or(sobelx.astype('unit8').astype('unit8'))
        filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_imag = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image
image_path = 'C:/Users/HP/Downloads/Image_annotation_AIEPCM2L3A1-3dd2 (1)/example.jpg' 
image = cv2.imread(image_path)

if image is None:
    print("Erroe:Image not found")
else:
    filter_type="orginal"

    print("Press the following leys to apply filters:")
    print("r - RedTint")
    print("g - green tint")
    print("b- Blue tint")
    print("s - Sobel edge detect ion")
    print("c - Canny Edge Dtetection")
    print(" - Quit")

    while True:

        filtered_image = apply_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type="red_tint"
        elif key ==ord('g'):
            filter_type ="green_tint"

        elif key == ord('b'):
            filter_type ="blue_tint"

        elif key == ord('s'):
            filter_type ="sobel"

        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! please use 'r', 'g', 'b', 's', 'c', or 'q'.")

cv2.destroyAllWindows()                            