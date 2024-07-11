import os 
import base64

from flask import Flask,render_template,send_from_directory,send_file,request,jsonify
from function import getFilters ,getFrames,getStickers
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
            dpi = get_image_dpi(app.instance_path+'/editbyfilter/'+image)
            convertImage(int(index),app.instance_path+'/editbyfilter/'+image,dpi,app.instance_path+'/editbyfilter/'+image)

        else:
            dpi = get_image_dpi(app.instance_path+'/uploads/'+image)
            convertImage(int(index),app.instance_path+'/uploads/'+image,dpi,app.instance_path+'/editbyfilter/'+image)
    elif request.method == 'GET':
        return  send_from_directory(f"{os.path.join(app.instance_path,'editbyfilter')}",filename.split('?')[0])


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
app.run(host='0.0.0.0',port=5000)