from face_app import db

class Face(db.Model):
  username = db.Column(db.String(64), primary_key=True)
  user_image_url = db.Column(db.String(120), index=True, unique=True)
  def __repr__(self):
    return '<User %r>' % self.username

def init():
  db.create_all()