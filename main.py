import os 
import base64
from pathlib import Path
import shutil
from flask import Flask,render_template,send_from_directory,send_file,request,jsonify
from function import getFilters ,getFrames,getStickers
from editImage import filterDic,convertImage ,getImageSize
from time import sleep
from testPrinter import print_image
path_save_photos = Path.home() / "Pictures" / "imageEditor"
app = Flask(__name__)

try:
    if  Path.exists(path_save_photos):
        os.rmdir(path_save_photos)
except:
    pass
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
#  if (imgElement.complete) {
#             convertImageToBase64(imgElement);
#         }

@app.route('/')
def hello():
    return render_template('index.html',filters =getFilters(),frames=getFrames() ,stickers = getStickers(),src='./images/Filters/Blur.png')

@app.route('/css/<filename>')
def sendCss(filename):
    return send_from_directory('static/css',filename)
@app.route('/js/<filename>')
def sendJs(filename):
    return send_from_directory('static/js',filename)
@app.route('/base64' ,methods=["POST"])
def savePhoto(): 
    data = request.get_json()
    
    print(data.keys())
    # image_data = data['image']
    
    image_name = data['Name']
    image_data = data['image']
    
    base64_image = image_data.split(',')[1]

    image_bytes = base64.b64decode(base64_image)
    path = os.path.join(os.path.join(app.instance_path,'editbyfilter'), image_name)
    print(path)
    with open(path, 'wb') as f:
        f.write(image_bytes)

    path = os.path.join(os.path.join(app.instance_path,'uploads'), image_name)
    print(path)
    with open(path, 'wb') as f:
        f.write(image_bytes)

    
    return jsonify({'Success:':"done"})

@app.route('/images/Svg/<filename>') 
def sendImages(filename): 
    # return send_file(f"image\{filename}")
    return send_from_directory('images/Svg',filename)
@app.route('/images/Filters/<filename>')
def sendFilters(filename):
    return send_from_directory('images/Filters',filename)
@app.route('/images/Stickers/<filename>')
def sendStickers(filename):
    return send_from_directory('images/Stickers',filename)

@app.route('/images/Frames/<filename>')
def sendFrames(filename):
    return send_from_directory('images/Frames',filename)

@app.route('/filter/<filename>' ,methods=['POST','GET'])
def applyFilter(filename):
    if request.method == 'POST':
        print(request.json)
        filterDic[request.json.get('filter')](request.json.get('imageList'),app.instance_path)
        return jsonify({'data':"done"})
    elif request.method =='GET':
        return  send_from_directory(f"{os.path.join(app.instance_path,'editbyfilter')}",filename.split('?')[0])

@app.route('/resize/<filename>',methods=['POST','GET'])
def applyresize(filename):
    if request.method =='POST':
        image = request.json.get('image','')
        index = request.json.get('sizeIndex','')
        if(os.path.exists(app.instance_path+'/editbyfilter/'+image)):
            convertImage(int(index),app.instance_path+'/editbyfilter/'+image,72,app.instance_path+'/editbyfilter/'+image)
        else:
            convertImage(int(index),app.instance_path+'/uploads/'+image,72,app.instance_path+'/editbyfilter/'+image)
        return "done"
    elif request.method == 'GET':
        return  send_from_directory(f"{os.path.join(app.instance_path,'editbyfilter')}",filename.split('?')[0])

@app.route('/printer',methods=['POST'])
def printer():
    print(request.json)
    images = request.json.get('image','')
    if images:
        for image_name in images:
            size =getImageSize(app.instance_path+'/editbyfilter/'+image_name)
            width_in_cm =round(size[0]*2.54/72,1)
            height_in_cm =round(size[1]*2.54/72,1)
            path_image = app.instance_path+'/editbyfilter/'+image_name
            rotate_img= (width_in_cm > height_in_cm)
            offset_x_cm =0
            offset_y_cm =0
            # print_image(path_image,width_in_cm,height_in_cm,rotate_img ,offset_x_cm,offset_y_cm)

    return jsonify({'data':"done"})
@app.route('/ImageUploaded' , methods=['POST'])
def handle():
    files = request.files.getlist('files')
    print(app.instance_path)
    print(files)
    for file in files:
        file.save(os.path.join(os.path.join(app.instance_path,'uploads'), file.filename))
    return "as"

@app.route('/FrameUploaded' , methods=['POST'])
def handleFrame():
    files = request.files.getlist('files')
    path = app.instance_path.replace('\instance',"")
    path += "\images\Frames\\"
    print(path)
    print("hello")
    print(files)
    for file in files:
        number = len(os.listdir(path))+1
        print(number)
        file.save(f"{path}frame ({number}).png")
    return "as"
@app.route('/save',methods=['POST'])
def save():
    print(path_save_photos,Path.exists(path_save_photos))
    if Path.exists(path_save_photos):
        if os.listdir(path_save_photos):
            for i in os.listdir(path_save_photos):
                os.remove('{}/{}'.format(path_save_photos,i))
        os.rmdir(path_save_photos)
    sleep(0.1)
    shutil.copytree(os.path.join(app.instance_path,'editbyfilter'),path_save_photos)
    return "ok"


app.run(host='0.0.0.0',port=5000 ,debug=True)