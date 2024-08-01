from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current
# from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coursePage.db"
db = SQLAlchemy(app)

class coursePage(db.Model):
	Sno = db.Column(db.Integer, primary_key = True)
	Uname = db.Column(db.String(20), nullable = False)
	Upass = db.Column(db.String(20), nullable = False)
	Ldate = db.Column(db.DateTime, default = datetime.now(timezone.utc))

def __repr__(self) -> str:
	return f"<coursePage(Uname='{self.Uname}', Upass ='{self.Upass}', Ldate='{self.Ldate}')>"

@app.route("/")
@app.route("/home")
def hello():
	# return "<h1>Hello nanba</h1>"
	return render_template("index.html")

@app.route('/signUp')
def signUp():
	datenow = (datetime.now(timezone.utc))
	details = coursePage(Uname = "PTGG", Upass = "ptgGamer", Ldate = datenow)
	db.session.add(details)
	db.session.commit()
	return render_template("signUp.html")

@app.route("/login")
def signIn():
	# return "<h1>Hello Nanba</h1><br><P>Vanakkam da mapla</P>"
	return render_template("logIn.html")

@app.route("/courses")
def course():
	return render_template("courses.html")

@app.route("/user")
def user():
	alldata = coursePage.query.all()
	print(alldata)
	return render_template('Users.html',alldata = alldata)

@app.route("/show")
def show():
	return 'this is data to show open terminal'

if __name__ == "__main__":
	app.run(debug = True)