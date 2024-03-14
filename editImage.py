
import cv2
import numpy as np


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
# loadImage= cv2.imread('./testImage.png')
# # loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)
# inverted_image = cv2.bitwise_not(loadImage)# Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
# # Emboss_Effect_Img = cv2.filter2D(src=loadImage, kernel=Emboss_Kernel, ddepth=-1)
# cv2.imwrite('./imageResult/Black.png',inverted_image)

# #Sharpening Filter
# Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# Sharpen_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sharpen_Kernel, ddepth=-1)
# cv2.imwrite('./imageResult/Sharpen_Effect_Img.png',Sharpen_Effect_Img)

# #Sepia Filter
# Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
# Sepia_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sepia_Kernel, ddepth=-1)
# cv2.imwrite('./imageResult/Sepia_Effect_Img.png',Sepia_Effect_Img)

# #Blur Filter 
# Blur_Effect_Img = cv2.GaussianBlur(loadImage, (35, 35), 0)
# cv2.imwrite('./imageResult/Blur_Effect_Img.png',Blur_Effect_Img)
