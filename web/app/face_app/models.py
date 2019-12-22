from face_app import db

class Face(db.Model):
  facename = db.Column(db.String(64), primary_key=True)
  face_image_url = db.Column(db.String(120), index=True, unique=True)
  def __repr__(self):
    return '<User %r>' % self.facename

def init():
  db.create_all()