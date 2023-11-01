# from datetime import datetime
from flask import Flask, flash, request,render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = r'F:\IIT Project\static\upload'
ALLOWED_EXTENSIONS = {"mp3", '3gp', 'm4a', 'wav' , 'm3u' , 'ogg'}

app = Flask(__name__)
app.config['SECRET_KEY']= 'supersecretkey'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
       
             
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return render_template('Choose.html')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            # return 'File uploaded successfully'
            return render_template('Uploaded.html')

        else:
            return render_template('Extension.html')
    
    return render_template('index.html')
    # return redirect(url_for('allowed_file'))
    # return 'hello'

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')
    # return redirect("/Home")

@app.route('/')
def index():
    return render_template('index.html')
    # return redirect("/index" )

@app.route('/SignIn')
def SignIn():
    return render_template('SignIn.html')

    
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
