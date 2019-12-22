from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('face_app.config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
import face_app.views