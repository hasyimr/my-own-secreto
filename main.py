from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300), unique=False, nullable=False)

db.create_all()

@app.route("/")
def home():
    return render_template("index.html")