import face_recognition
import cv2
import numpy as np

def convert_face(original_path, convert_path):
  print(original_path)
  print(convert_path)
  origin = cv2.imread(original_path)
  face = cv2.imread(convert_path)
  print(origin.shape)
  print(face.shape)
  rgb_origin = origin[:, :, ::-1]

  face_locations = face_recognition.face_locations(rgb_origin)

  if(face_locations):
    for (top, right, bottom, left) in face_locations:
      diff = 0
      top += diff
      right -= diff
      bottom -= diff
      left += diff

      x_size = right - left
      y_size = bottom - top
      print('top:' + str(top) + ' bottom:' + str(bottom) + ' right:' + str(right) + ' left:' + str(left))
      print('x_size:' + str(x_size) + ' y_size:' + str(y_size))
      resize_face = cv2.resize(face, (x_size, y_size))
      origin[top:bottom, left:right] = resize_face
    cv2.imwrite(original_path, origin)
    return True
  else:
    return False
