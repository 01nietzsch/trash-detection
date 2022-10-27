# differents imports
import cv2
import matplotlib.pyplot as plt


# lecture de la camera 
frame = cv2.VideoCapture(0)

while True:
    ret, img = frame.read()
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# transformer la video en image noir et blanc
frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(frame, cmap='gray')
plt.show()


image =cv2.imread(img)
cv2.waitKey(0)

edged = cv2.Canny(image, 30, 200)
cv2.waitKey(0)



contours,hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)




# fermer la camera
frame.release()
cv2.destroyAllWindows()