import os

from flask import Flask, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_sharing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAIL_SERVER'] = 'yadavlaxit21@gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'Laxit Yadav'
app.config['MAIL_PASSWORD'] = 'Laxu@223344'
app.config['BASE_URL'] = 'http://127.0.0.1:5000'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

# Ensure the uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('login.html')  # This renders the login.html file

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Handle user signup logic here
        return redirect(url_for('index'))  # Redirect to login page after signup
    return render_template('signup.html')  # This renders the signup.html file

@app.route('/verify/<int:user_id>')
def verify_email(user_id):
    # Logic for email verification
    return render_template('verify.html', user_id=user_id)  # Renders verify.html

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload logic
        return redirect(url_for('index'))  # Redirect to login page after upload
    return render_template('upload.html')  # This renders the upload.html file

if __name__ == '__main__':
    app.run(debug=True)