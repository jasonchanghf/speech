from flask import Flask
from flask import flash, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return 'hello'

ALLOWED_EXTENSIONS = set(['wav'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/recognition',methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            flash(file.filename)
            return redirect(url_for('recognition'))
    return render_template('speech.html')
