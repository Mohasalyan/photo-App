import os 
from flask import Flask,render_template,send_from_directory,send_file,request,jsonify
from function import getFilters
from editImage import filterDic,get_image_dpi,convertImage
app = Flask(__name__)
try:
    files_uploaded_before = os.listdir(os.path.join(app.instance_path,'uploads'))
    if files_uploaded_before:
        for file in files_uploaded_before:
            os.remove(f"{os.path.join(app.instance_path,'uploads')}\{file}")
except:
    os.mkdir(app.instance_path)
    os.mkdir(app.instance_path+'/uploads')

try:
    files_uploaded_before = os.listdir(os.path.join(app.instance_path,'editbyfilter'))
    if files_uploaded_before:
        for file in files_uploaded_before:
            os.remove(f"{os.path.join(app.instance_path,'editbyfilter')}\{file}")
except:
    try:
        os.mkdir(app.instance_path)
    except:
        pass
    os.mkdir(app.instance_path+'/editbyfilter')


@app.route('/')
def hello():
    return render_template('index.html',filters =getFilters(),src='./images/Filters/Blur.png')

@app.route('/css/<filename>')
def sendCss(filename):
    return send_from_directory('static/css',filename)
@app.route('/js/<filename>')
def sendJs(filename):
    return send_from_directory('static/js',filename)

@app.route('/images/Svg/<filename>') 
def sendImages(filename): 
    # return send_file(f"image\{filename}")
    return send_from_directory('images/Svg',filename)
@app.route('/images/Filters/<filename>')
def sendFilters(filename):
    return send_from_directory('images/Filters',filename)

@app.route('/filter/<filename>' ,methods=['POST','GET'])
def applyFilter(filename):
    if request.method == 'POST':
        filterDic[request.json.get('filter')](request.json.get('imageList'),app.instance_path)
        return jsonify({'data':"done"})
    elif request.method =='GET':

        return  send_from_directory(f"{os.path.join(app.instance_path,'editbyfilter')}",filename)

@app.route('/resize/<filename>',methods=['POST','GET'])
def applyresize(filename):
    if request.method =='POST':
        image = request.json.get('image','')
        index = request.json.get('sizeIndex','')
        if(os.path.exists(app.instance_path+'/editbyfilter/'+image)):
            dpi = get_image_dpi(app.instance_path+'/editbyfilter/'+image)
            convertImage(int(index),app.instance_path+'/editbyfilter/'+image,dpi,app.instance_path+'/editbyfilter/'+image)

        else:
            dpi = get_image_dpi(app.instance_path+'/uploads/'+image)
            convertImage(int(index),app.instance_path+'/uploads/'+image,dpi,app.instance_path+'/editbyfilter/'+image)
    elif request.method == 'GET':
        return  send_from_directory(f"{os.path.join(app.instance_path,'editbyfilter')}",filename)


    return jsonify({'data':"done"})
@app.route('/ImageUploaded' , methods=['POST'])
def handle():
    files = request.files.getlist('files')
    print(files)
    print(app.instance_path)
    for file in files:
        file.save(os.path.join(os.path.join(app.instance_path,'uploads'), file.filename))
    return "as"
app.run(host='0.0.0.0',port=5000)