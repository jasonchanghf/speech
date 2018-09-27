from flask import Flask
from flask import flash, render_template, request, redirect, url_for
from config import Config
from forms import UploadForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'hello'

ALLOWED_EXTENSIONS = set(['wav'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/recognition',methods=['GET','POST'])
def recognition():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'files', filename
        ))
        return redirect(url_for('recognition'))

    return render_template('recognition.html', form=form)