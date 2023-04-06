import os
import logging
import sys
import mimetypes

from flask import Flask, flash, send_from_directory
from flask import render_template, redirect
from werkzeug.utils import secure_filename
from flask import request


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


app = Flask(__name__)
app.secret_key = b'_hvh.,kj/m,'

ALLOWED_EXTENSIONS = {'mp3', 'oog', 'wav'}


def allowed_file(filename):
    logger.debug(mimetypes.guess_type(filename)[0])
    # logger.debug(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def main_page():
    list_singls = 'upload/'
    with os.scandir(list_singls) as files:
        files = [file.name for file in files if file.is_file()]

    return render_template('index.html', list_singls=files)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['the_file']

        if allowed_file(file.filename):
            file.save(os.getcwd() + "/upload/{}".format(secure_filename(file.filename)))
        else:
            flash("Неверный формат файла")

    return redirect('/')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(os.getcwd() + "/upload/", name)
