
import cv2
import numpy as np
from PIL import Image


def EmbossFilter(imageList,dirction):
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
        Emboss_Effect_Img = cv2.filter2D(src=loadImage, kernel=Emboss_Kernel, ddepth=-1)
        cv2.imwrite('./imageResult/Emboss_Effect_Img.png',Emboss_Effect_Img)
def BlurFilter(imageList,dirction):
      print(imageList,dirction)
      for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        Blur_Effect_Img = cv2.GaussianBlur(loadImage, (35, 35), 0)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",Blur_Effect_Img)
        print("done")
def SepiaFilter(imageList,dirction):
    print(imageList,dirction)
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        Sepia_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sepia_Kernel, ddepth=-1)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",Sepia_Effect_Img)
def SharpenFilter(imageList,dirction):
    print(imageList,dirction)
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        Sharpen_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sharpen_Kernel, ddepth=-1)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",Sharpen_Effect_Img)
def EmbossFilter(imageList,dirction):
    print(imageList,dirction)
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
        Emboss_Effect_Img = cv2.filter2D(src=loadImage, kernel=Emboss_Kernel, ddepth=-1)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",Emboss_Effect_Img)
def BlackWhiteFilter(imageList,dirction):
     for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        _, bw_image = cv2.threshold(loadImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",bw_image)
def edgeFilter(imageList,dirction):
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
        edges = cv2.Canny(loadImage, 50, 150)
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",edges)
def InvertedFilter(imageList,dirction):
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        inverted_image = cv2.bitwise_not(loadImage)# Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",inverted_image)
def Origin(imageList,dirction):
    for image in imageList:
        loadImage= cv2.imread(f"{dirction}/uploads/{image}")
        cv2.imwrite(f"{dirction}/editbyfilter/{image}",loadImage)

filterDic ={ 
    'Blur':BlurFilter,
    'Sepia':SepiaFilter,
    'Sharpen':SharpenFilter,
    'Emboss':EmbossFilter,
    'BlackWhite':BlackWhiteFilter,
    'Edge':edgeFilter,
    'Inverted':InvertedFilter,
    'Origin':Origin
}



def convertP2C(pixel,dpi):
    return pixel / dpi

def convertC2P(cm,dpi):
    return cm * dpi
    


def convertImage(index,path,dpi,save):
    img = cv2.imread(path)
    print(path)
    resizeData=[]
    if img.shape[0] > img.shape[1]:
        resizeData = [(7.5,10),(10,15),(15,20),]
    else :
        resizeData = [(10,7.5),(15,10),(20,15),]
    
    shape = (int(resizeData[index][0] *72/2.54),int(resizeData[index][1] *72/2.54))
    print(dpi,shape,resizeData[0])
    resized_image = cv2.resize(img,shape)
    cv2.imwrite(save,resized_image)



def getImageSize(path):
    return cv2.imread(path).shape
# convertImage(0,'C:/Users/XPRISTO/Desktop/306735038_3084260165054148_6564624860134792767_n.jpg',(96,96))
    
# print(get_image_dpi('E:/ImageEditor/ImageEditor/instance/uploads/306735038_3084260165054148_6564624860134792767_n.jpg'))


# loadImage= cv2.imread("C:\Users\XPRISTO\Desktop\testImage.png")
# loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
# _, bw_image = cv2.threshold(loadImage, 127, 255, cv2.THRESH_BINARY)
# cv2.imwrite(f"./BlackWhite.jpg",bw_image)