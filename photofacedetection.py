import cv2
print(cv2.__version__)

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test.png')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
# Display the output
cv2.imshow('img', img)
cv2.waitKey()

# Display the output
cv2.imshow('img', img)

while True:
    key = cv2.waitKey(1)  # Check for a key event every 1 millisecond

    if key == 27:  # Check for the Esc key (ASCII code 27)
        break  # Exit the loop if Esc is pressed

cv2.destroyAllWindows()  # Close all OpenCV windows