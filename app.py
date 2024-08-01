from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
	# return "<h1>Hello nanba</h1>"
	return render_template("index.html")

@app.route('/run-script')
def signUp():
	return render_template("signUp.html")

@app.route("/login")
def signIn():
	# return "<h1>Hello Nanba</h1><br><P>Vanakkam da mapla</P>"
	return render_template("logIn.html")

@app.route("/courses")
def course():
	return render_template("courses.html")
	
if __name__ == "__main__":
	app.run(debug = True)