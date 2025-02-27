from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from PIL import Image

# Create the Flask app
app = Flask(__name__, template_folder='./app/templates', static_folder='./app/static')

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

UPLOAD_FOLDER = './app/static/uploads'
THUMBNAIL_FOLDER = 'thumbnails'
CATEGORIES = ['torturi', 'prajituri']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

for category in CATEGORIES:
    os.makedirs(os.path.join(UPLOAD_FOLDER, category), exist_ok=True)
    os.makedirs(os.path.join(UPLOAD_FOLDER, category, THUMBNAIL_FOLDER), exist_ok=True)

def create_thumbnail(image_path, thumbnail_path):
    with Image.open(image_path) as img:
        img.thumbnail((200, 200))
        img.save(thumbnail_path)

# Allowed users with hashed passwords for demonstration
users = {
    "admin": generate_password_hash("admin"),
    "user": generate_password_hash("user")
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    # Redirectioneaza utilizatorii autentificati la pagina de autentificare
    if session.get("user_authenticated"):
        return redirect(url_for("login"))
    
    gallery = {}
    # Creeaza galeria de imagini pentru fiecare categorie
    for category in CATEGORIES:
        thumbnail_path = os.path.join(UPLOAD_FOLDER, category, THUMBNAIL_FOLDER)
        if os.path.exists(thumbnail_path):
            images = os.listdir(thumbnail_path)
            gallery[category] = images
    return render_template("index.html", gallery=gallery)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_password_hash = users.get(username)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['user_id'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route("/upload", methods=["GET", "POST"])
def upload():
    # Check if the user is authenticated by checking 'user_id' in session
    if 'user_id' not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        file = request.files.get("image")
        new_name = request.form.get("name")
        category = request.form.get("category", "uncategorized").lower()

        if file and allowed_file(file.filename):
            filename = new_name if new_name else file.filename
            category_path = os.path.join(UPLOAD_FOLDER, category)
            file_path = os.path.join(category_path, filename)
            thumbnail_path = os.path.join(category_path, THUMBNAIL_FOLDER, filename)
            
            file.save(file_path)
            create_thumbnail(file_path, thumbnail_path)
            flash('File successfully uploaded')
            return redirect(url_for('index'))
    
    return render_template("upload.html", categories=CATEGORIES)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
