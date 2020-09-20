import os
import shutil
#import zipfile
#from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename



from pca import pca_compress
from k_means import k_means_raster

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__,template_folder='template')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'tif'])

#def zipdir(path, ziph):
    # ziph is zipfile handle
 #   for root, dirs, files in os.walk(path):
  #      for file in files:
   #         ziph.write(os.path.join(root, file))

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
        return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
        if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #print('upload_image filename: ' + filename)
                flash('Orthophoto successfully uploaded')
                # flash('Performing Spectral Analysis on Image')
                print(filename)
                pca = pca_compress(filename)
                k_means = k_means_raster()
                return render_template('index.html', filename=filename, pca_status = pca, k_means_status = k_means)
        else:
                flash('Allowed image types are -> png, tif, jpg, jpeg, gif')
                return redirect(request.url)

# @app.route('/download-files', methods=['GET'])
# def return_file():
#       zipf = zipfile.ZipFile('assets.zip', 'w', zipfile.ZIP_DEFLATED)
#       zipdir('./static/assets', ziph)
#       return send_file('./static', as_attachment=True, attachment_filename="pca-compressed.jpeg")


@app.route('/download')
def download_file():
        #zipf = zipfile.ZipFile('static/assets.zip', 'w', zipfile.ZIP_DEFLATED)
        #zipdir('./static/assets', zipf)
        shutil.make_archive("static/assets", "zip", "static/assets")
        path = "static/assets.zip"
        return send_file(path, as_attachment=True, cache_timeout=0)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8044, debug=True)
