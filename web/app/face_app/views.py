from flask import request, redirect, url_for, render_template, flash
from face_app import app, db
from face_app import face
from werkzeug.utils import secure_filename

@app.route('/')
def hello():
  return render_template('hello.html')

@app.route('/convert', methods=['GET'])
def convert():

  return render_template('convert.html')

@app.route('/result', methods=['POST'])
def result():
  print('result')
  f = request.files['image']
  
  original_path = '/static/original.' + f.filename.rsplit('.', 1)[1].lower()

  f.save('face_app' + original_path)
  face_path = 'face_app/static/convert.jpg'
  if face.convert_face('face_app'+ original_path, face_path):
    return render_template('result.html', image_path=original_path)
  else:
    flash('顔が見つかりません')
    return redirect(url_for('convert'))

@app.route('/edit')
def edit():
  return render_template('edit.html')

@app.route('/add', methods=['POST'])
def add_face():
  return render_template('edit.html')
