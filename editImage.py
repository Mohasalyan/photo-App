
import cv2
import numpy as np

loadImage= cv2.imread('./testImage.png')
# loadImage = cv2.cvtColor(loadImage,cv2.COLOR_BGR2RGB)

#Emboss Filter
Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
Emboss_Effect_Img = cv2.filter2D(src=loadImage, kernel=Emboss_Kernel, ddepth=-1)
cv2.imwrite('./imageResult/Emboss_Effect_Img.png',Emboss_Effect_Img)

#Sharpening Filter
Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
Sharpen_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sharpen_Kernel, ddepth=-1)
cv2.imwrite('./imageResult/Sharpen_Effect_Img.png',Sharpen_Effect_Img)

#Sepia Filter
Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
Sepia_Effect_Img = cv2.filter2D(src=loadImage, kernel=Sepia_Kernel, ddepth=-1)
cv2.imwrite('./imageResult/Sepia_Effect_Img.png',Sepia_Effect_Img)

#Blur Filter 
Blur_Effect_Img = cv2.GaussianBlur(loadImage, (35, 35), 0)
cv2.imwrite('./imageResult/Blur_Effect_Img.png',Blur_Effect_Img)
