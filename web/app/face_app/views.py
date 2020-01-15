from flask import request, redirect, url_for, render_template, flash
from face_app import app, db
from face_app import face
from face_app.models import Face
from werkzeug.utils import secure_filename
import time

@app.route('/hello')
def hello():
  return render_template('hello.html')

@app.route('/', methods=['GET'])
def convert():
  faces = Face.query.all()
  return render_template('convert.html', faces=faces)

@app.route('/result', methods=['POST'])
def result():
  f = request.files['image']
  original_path = '/static/original.' + f.filename.rsplit('.', 1)[1].lower()
  face_name = request.form['facename']
  if face_name == 'obama':
    face_path = 'face_app/static/sample_face.jpg'
  else:
    face_path = 'face_app' + Face.query.get(face_name).face_image_url
  f.save('face_app' + original_path)
  # face_path = 'face_app/static/convert.jpg'
  if face.convert_face('face_app'+ original_path, face_path):
    return render_template('result.html', image_path=original_path+ '?'+str(int(time.time())))
  else:
    flash('顔が見つかりません')
    return redirect(url_for('convert'))

@app.route('/edit')
def edit():
  return render_template('edit.html')

@app.route('/add', methods=['POST'])
def add_face():
  f = request.files['image']
  print(request.form['facename'])
  add_image_path = '/static/'+request.form['facename'] + '.'+ f.filename.rsplit('.', 1)[1].lower()
  f.save('face_app' + add_image_path)
  if(face.face_detection('face_app' + add_image_path)):
    newFace = Face(facename=request.form['facename'],
                   face_image_url=add_image_path)
    db.session.add(newFace)
    db.session.commit()
    return render_template('edit_result.html', image_path=add_image_path)
  else:
    flash('顔が検出されなかった、複数あります')
    return redirect(url_for('edit'))
