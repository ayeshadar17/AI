import cv2

image=cv2.imread('C://Users//HP//Downloads//Intro_to_Computer_Vision___OpenCV_asset-e753 (2)//example.jpg')

cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL) #Create a resozable window
cv2.resizeWindow('Loaded Image',800,500) #Set the window size to 800 (width x height)

cv2.imshow('Loaded Image',image)
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() #Close the window

print(f"Image Dimentions:[image.shape]") # Height, Width, Channels