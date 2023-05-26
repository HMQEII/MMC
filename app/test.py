# import cv2
# import numpy as np

# # Load the hat image
# hat = cv2.imread("D:\Jerin Docs\miniproject\3.png")

# # Check that the hat image has three channels (RGB)
# if hat is not None and hat.shape[2] == 3:
#     print("The hat image has three channels (RGB).")
# else:
#     print("The hat image does not have three channels or could not be loaded.")
#     exit()

# # Load the cascade classifier for face detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# # Open the camera
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture a frame from the camera
#     ret, frame = cap.read()
    
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the grayscale frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
#     # Loop over the faces
#     for (x, y, w, h) in faces:
#         # Resize the hat to match the size of the face
#         hat = cv2.resize(hat, (w, int(0.35 * h)))
        
#         # Calculate the ROI for the hat
#         roi = frame[y - int(0.35 * h):y, x:x + w]
        
#         # Create a mask for the hat
#         mask = np.zeros(roi.shape[:-1], dtype=np.uint8)
#         mask = cv2.fillPoly(mask, [np.array([[0, 0], [w, 0], [w, int(0.35 * h)], [0, int(0.35 * h)]])], 1)
        
#         # Perform alpha blending between the hat and the ROI
#         hat = cv2.bitwise_and(hat, hat, mask=mask)
#         roi = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
#         roi = cv2.addWeighted(roi, 1, hat, 0.5, 0)
#         frame[y - int(0.35 * h):y, x:x + w] = roi
    
#     # Display the augmented frame
#     cv2.imshow("Frame", frame)
    
#     # Check if the user pressed the 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close the window
# cap.release()
# cv2.destroyAllWindows()



################# Necklace #################
# import cv2
# import numpy as np

# # Load the necklace image
# necklace = cv2.imread('D:\Jerin Docs\miniproject\1.png')

# # cv2.imshow('image',necklace)
# # print(necklace)
# # Get the dimensions of the necklace
# necklace_h, necklace_w, necklace_c = necklace.shape

# # Create the mask for the necklace
# necklace_mask = necklace[:, :, 3]

# # Set up the video capture
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture a frame from the camera
#     ret, frame = cap.read()

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the frame
#     faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml").detectMultiScale(gray, 1.3, 5)

#     # Iterate over the faces
#     for (x, y, w, h) in faces:
#         # Get the neck position
#         neck_y = int(y + h * 0.75)
#         neck_x = int(x + w * 0.5)
#         neck_w = int(w * 0.6)
#         neck_h = int(h * 0.1)

#         # Resize the necklace to fit the neck
#         resized_necklace = cv2.resize(necklace, (neck_w, neck_h), interpolation = cv2.INTER_CUBIC)
#         resized_necklace_mask = cv2.resize(necklace_mask, (neck_w, neck_h), interpolation = cv2.INTER_CUBIC)

#         # Create an RGBA version of the frame
#         frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

#         # Get the ROI for the necklace
#         roi = frame_rgba[neck_y:neck_y + neck_h, neck_x:neck_x + neck_w]

#         # Create the mask for the necklace
#         necklace_mask_inv = cv2.bitwise_not(resized_necklace_mask)

#         # Black out the area behind the necklace in the ROI
#         roi = cv2.bitwise_and(roi, roi, mask = necklace_mask_inv)

#         # Add the necklace to the ROI
#         roi = cv2.add(roi, resized_necklace)

#         # Put the ROI back into the frame
#         frame_rgba[neck_y:neck_y + neck_h, neck_x:neck_x + neck_w] = roi

#         # Convert the frame back to BGR
#         frame = cv2.cvtColor(frame_rgba, cv2.COLOR_BGRA2BGR)

#     # Show the augmented frame
#     cv2.imshow('Necklace Augmentation', frame)

#     # Break the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release
# cap.release()
# cv2.destroyAllWindows()


########## Glasess ###########
import cv2
import dlib

# Load the pre-trained facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the glasses image
glasses_img = cv2.imread("C:\Users\SHASHANK\Desktop\Virtual shopping\app\static\app\images\productblue.jpg", -1)

# Start the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = detector(gray)
    
    # Loop through all detected faces
    for face in faces:
        # Get the facial landmarks for the face
        landmarks = predictor(gray, face)
        
        # Get the coordinates of the left and right eye landmarks
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)
        
        # Calculate the width and height of the glasses image based on the eye distance
        eye_distance = right_eye[0] - left_eye[0]
        glasses_width = int(1.5 * eye_distance)
        glasses_height = int(0.7 * eye_distance)
        
        # Resize the glasses image to the calculated size
        glasses_resized = cv2.resize(glasses_img, (glasses_width, glasses_height))
        
        # Calculate the coordinates of the top-left corner of the glasses image
        glasses_x = left_eye[0] - int(0.25 * eye_distance)
        glasses_y = left_eye[1] - int(0.35 * eye_distance)
        
        # Overlay the glasses image on top of the face
        for i in range(glasses_resized.shape[0]):
            for j in range(glasses_resized.shape[1]):
                if glasses_resized[i, j, 3] != 0:
                    frame[glasses_y+i, glasses_x+j, :] = glasses_resized[i, j, :-1]
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


######### Hat ####################
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# # Load hat image
# hat = cv2.imread('D:\Jerin Docs\miniproject\j.png')
# # hat = cv2.imread('app\images\virtual\j.png')
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Convert to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     # Iterate over each detected face
#     for (x, y, w, h) in faces:
#         # Calculate hat position and size
#         hat_w = int(1.4 * w)
#         hat_h = int(0.77 * h)
#         hat_x1 = int(x - (hat_w-w)/2)
#         hat_x2 = int(x + w + (hat_w-w)/2)
#         hat_y1 = int(y - 0.77*h - (hat_h-h)/2)
#         hat_y2 = int(y - 0.77*h + hat_h + (hat_h-h)/2)
        
#         # Check if hat is within frame boundaries
#         if hat_x1 < 0 or hat_y1 < 0 or hat_x2 > frame.shape[1] or hat_y2 > frame.shape[0]:
#             continue
        
#         # Resize hat to fit face
#         hat_resized = cv2.resize(hat, (hat_x2-hat_x1, hat_y2-hat_y1))
#         hat_resized = cv2.cvtColor(hat_resized, cv2.COLOR_BGR2RGB)
#         hat_resized = cv2.cvtColor(hat_resized, cv2.COLOR_RGB2BGR)
#         hat_resized = cv2.resize(hat_resized, (hat_x2-hat_x1, hat_y2-hat_y1))

#         # Put hat on frame
#         frame[hat_y1:hat_y2, hat_x1:hat_x2] = hat_resized

#     # Display the resulting frame
#     cv2.imshow('frame', frame)

#     # Exit on press of 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture
# cap.release()
# cv2.destroyAllWindows()
