from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = "sad812734089"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300), unique=False, nullable=False)

class MessageForm(FlaskForm):

    user_message = StringField('Your Message for Me', validators=[DataRequired()])
    submit = SubmitField('Submit')

db.create_all()

@app.route("/", methods=["POST", "GET"])
def home():
    database = Comments.query.all()
    form = MessageForm()

    if form.validate_on_submit():
        messages = Comments(message=form.user_message.data)
        db.session.add(messages)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("index.html", form=form, database=database)

if __name__ == "__main__":
    app.run(debug=True)