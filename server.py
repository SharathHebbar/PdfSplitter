from flask import Flask,render_template,request
from flask.helpers import send_file
import pdfsplitter

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("file_upload.html")

@app.route('/success',methods =['POST'])
def success():
    global st
    global en
    global fname
    data = request.form
    st = int(data['start'])
    en = int(data['end'])
    f = request.files['file']
    fname = f.filename
    f.save(fname)
    return render_template('success.html',start= st,end = en,name = fname)

@app.route('/convert')
def cropper():
    pdfsplitter.cropper(st-1,en-1,fname)
    return render_template('download.html')

@app.route('/download')
def download():
    filename = fname.split(".")[0]+"cropped.pdf"
    return send_file(filename,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)