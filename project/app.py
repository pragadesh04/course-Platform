from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os
from PIL import Image  # Make sure Pillow is imported correctly
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, length, ValidationError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Data(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Data('{self.username}', '{self.password}')"

# Directory paths
image_dir = 'static/images/output'
thumbnail_dir = 'static/thumbnails'

@app.route('/')
def image_gallery():
    # Get a list of image files from the specified directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    
    # Sort the list of image files by last modified date (newest first)
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_dir, x)), reverse=True)

    # Get the page number from the query string (default to 1)
    page = int(request.args.get('page', 1))

    # Calculate the total number of pages
    total_pages = (len(image_files) + 99) // 100  # Ensure a maximum of 100 images per page

    # Slice the image list to display images for the current page
    start_idx = (page - 1) * 100
    end_idx = start_idx + 100
    current_images = image_files[start_idx:end_idx]

    # Generate thumbnails for the current page if they don't exist
    generate_thumbnails(current_images)

    return render_template('index.html', current_thumbnails=current_images, total_pages=total_pages, page=page)

def generate_thumbnails(image_list):
    for image in image_list:
        thumbnail_path = os.path.join(thumbnail_dir, image)
        if not os.path.exists(thumbnail_path):
            try:
                original_image_path = os.path.join(image_dir, image)
                original_image = Image.open(original_image_path)
                max_width = 200  # Define your desired thumbnail width
                max_height = 200  # Define your desired thumbnail height
                original_image.thumbnail((max_width, max_height), Image.ANTIALIAS)
                original_image.save(thumbnail_path)
            except Exception as e:
                print(f"Error generating thumbnail for {image}: {str(e)}")

@app.route("/courses")
def course():
    return render_template("courses.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
