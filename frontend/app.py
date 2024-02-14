from flask import Flask, render_template, request
import os
import numpy as np
from werkzeug.utils import secure_filename
import subprocess
import os


# Get the path of the current script
script_path = os.path.abspath("PostGreDataInput.py")

print(f"The path of the script is: {script_path}")

app = Flask(__name__)
number_of_files = 0
# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', filenames=[])

@app.route('/upload', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return "No file part"
    
    files = request.files.getlist('files[]')
    number_of_files = np.size(files)
    print(number_of_files)

    filenames = []
    for index, file in enumerate(files, 1):  # Start index from 1
        if file.filename == '':
            return "No selected file"

        if file and allowed_file(file.filename):
            # Generate new filename with file number
            new_filename = f"2012_sample_construction_file_{number_of_files}.xlsx"
            filename = secure_filename(new_filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            filenames.append(filename)
        else:
            return "Invalid file format. Please upload .xlsx files only."

    return render_template('index.html', filenames=filenames)


if __name__ == '__main__':
    app.run(debug=True)
    subprocess.run(['python', script_path, str(number_of_files)])
