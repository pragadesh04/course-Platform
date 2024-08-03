from flask import Flask, request, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datas.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

# class data(db.model):
#     username = db.Column(db.String(20), primary_key = True)
#     password = db.Column(db.String(20), nullable = False)

def __repr__(self) -> str:
    return f"datas('{self.username}', '{self.password}')"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)