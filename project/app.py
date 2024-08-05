from flask import Flask, request, render_template, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)

# Configuring the SQLAlchemy Database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class data(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"datas('{self.username}', '{self.password}')"

# RegisterForm with correct validators
# class registerForm(FlaskForm):
#     username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
#     password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
#     submit = SubmitField("Register")

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/courses")
def course():
    return render_template("courses.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmPass = request.form.get('confirmPass')
        if(password == confirmPass):
            print("name: {}\npass: {}".format(username, password))
        else:
            print("Pasword does not match!!")
    return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
