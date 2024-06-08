import face_recognition
import cv2

# Load the image file
image = face_recognition.load_image_file("images/1.jpg")

# Find all the face locations in the image
face_locations = face_recognition.face_locations(image)

# Convert the image to BGR color (which OpenCV uses)
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Draw rectangles around each face
for (top, right, bottom, left) in face_locations:
    # Draw a rectangle around the face
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 0, 255), 2)

# Display the image with the faces highlighted
cv2.imshow('Found Faces', image_bgr)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
