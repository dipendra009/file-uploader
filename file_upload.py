from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['MAX_CONTENT_PATH'] = 1024*16

upload_path = 'uploads/'
os.makedirs(upload_path, exist_ok=True)

@app.route('/upload')
def uploader_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploading_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(upload_path, secure_filename(f.filename)))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)