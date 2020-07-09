import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #트랜잭션이 끝날 때마다 커밋을 함
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
        __tablename__ = 'test_table'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(32), unique=True)

@app.route('/')
def hello():
        return 'Hello World!'