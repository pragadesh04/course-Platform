from flask import Flask, request, render_template
# from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from flask_wtf import wtforms
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, length, ValidationError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class data(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(20), nullable = False)

# class registerForm(FlaskForm):
#     username = StringField("Username", validators=[input_required(), length(min=4, max=20)], render_kw={"placeholder":"Username"})
#     password = StringField("Username", validators=[input_required(), length(min=4, max=20)], render_kw={"placeholder":"Password"})
#     submit = SubmitField("Registered")

def __repr__(self) -> str:
    return f"datas('{self.username}', '{self.password}')"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)