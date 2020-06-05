"""
  @author: yigit.yildirim@boun.edu.tr

  Taken from Sentdex - Youtube: https://www.youtube.com/watch?v=535acCxjHCI&list=PLQVvvaa0QuDcDqgpLLJJM15NpIGNfrKY5
  * Sentdex is the best Youtube channel IMO (https://www.youtube.com/user/sentdex)

  pip install face_recognition
  pip install opencv-python
"""

import face_recognition
import os
import cv2

KNOWN_FACES_DIR = 'known_faces'
UNKNOWN_FACES_DIR = 'unknown_faces'

TOLERANCE = 0.2  # chance of labeling a face; higher tolerance higher num mistakes
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'  # CNN: Convolutional Neural Network. Another option 'hog'

print('loading known faces')
known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print('processing unknown faces')
for filename in os.listdir(UNKNOWN_FACES_DIR):
    image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        # compare encoding to every known face ancoding and return a list of booleans
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f'Match found: {match}')

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [255, 0, 0]
            cv2.rectangle(image_cv, top_left, bottom_right, color, FRAME_THICKNESS)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)

            cv2.rectangle(image_cv, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image_cv, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (200, 200, 200), FONT_THICKNESS)

    cv2.imshow(filename, image_cv)
    cv2.waitKey(1000)




