from flask import Flask,render_template,send_from_directory,send_file

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/images/<filename>') 
def sendImages(filename): 

    # return send_file(f"image\{filename}")
    return send_from_directory('images',filename)

app.run(host='0.0.0.0',port=5000)