import face_recognition
import cv2
import numpy as np

def convert_face(original_path, convert_path):
  origin = cv2.imread(original_path)
  face = cv2.imread(convert_path)
  rgb_origin = origin[:, :, ::-1]

  face_locations = face_recognition.face_locations(rgb_origin)

  if face_locations:
    for (top, right, bottom, left) in face_locations:
      diff = 0
      top += diff
      right -= diff
      bottom -= diff
      left += diff

      x_size = right - left
      y_size = bottom - top
      resize_face = cv2.resize(face, (x_size, y_size))
      origin[top:bottom, left:right] = resize_face
    cv2.imwrite(original_path, origin)
    return True
  else:
    return False

def face_detection(add_image_path):
  image = cv2.imread(add_image_path)
  rgb_image = image[:,:, ::-1]
  face_locations = face_recognition.face_locations(rgb_image)
  if len(face_locations) == 1:
    top, right, bottom, left = face_locations[0]
    face = image[top:bottom, left:right]
    cv2.imwrite(add_image_path, face)
    return True
  else:
    return False

# def convert_face(original_path, convert_path):
#   face_cascade = cv2.CascadeClassifier('face_app/static/haarcascade_frontalface_default.xml')
#   origin = cv2.imread(original_path)
#   face = cv2.imread(convert_path)
#   face_locations = face_cascade.detectMultiScale(origin)
#   if len(face_locations):
#     for (x, y, w, h) in face_locations:
#       resize_face = cv2.resize(face, (w, h))
#       origin[y:y+h, x:x+w] = resize_face
#     cv2.imwrite(original_path, origin)
#     return True
#   else:
#     return False
#   return 

# def face_detection(add_image_path):
#   face_cascade = cv2.CascadeClassifier('face_app/static/haarcascade_frontalface_default.xml')
#   image = cv2.imread(add_image_path)
#   face_locations = face_cascade.detectMultiScale(image)
#   if len(face_locations) == 1:
#     x, y, w, h = face_locations[0]
#     face = image[y:y+h, x:x+w]
#     cv2.imwrite(add_image_path, face)
#     return True
#   else:
#     return False
