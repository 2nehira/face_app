SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = 'sqlite:///face_app.db'
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tune:tune@localhost/face_app'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@db:3306/face_app'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@192.168.32.2:3306/face_app'

SECRET_KEY = 'secret key'