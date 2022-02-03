import os
import sys
import cv2
import pyzbar.pyzbar as pyzbar


def main():
    # print(sys.argv[0]) # FileName.py
    # print(sys.argv[1]) # First Value

    # imgfile = 'images/sample_00.png'
    imgfile = sys.argv[1]
    
    # os.system("curl " + sys.argv[1] + " > ./images/qrImage.png")   
    # imgfile = 'images/qrImage.png'

    img = cv2.imread(imgfile)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    pointX=0
    pointY=0
    baseLine=0
    
    scaleValue = 1
    splitValue = 1
    baseValue = 74
    baseSpace = 250
    baseSplit = 60
    
    decoded = pyzbar.decode(imgGray)
#     print(decoded)
    
    for d in decoded:
#         print(d.data.decode('utf-8'))
        pointX = d.rect[0]
        pointY = d.rect[1]
        baseLine = d.rect[2]
    
    # print(baseLine)
    scaleValue = baseLine/baseValue
    # print(scaleValue)
    splitValue = (int)(baseSplit*scaleValue)
    pointX = pointX + (int)(baseSpace*scaleValue)
    pointY = pointY + (int)(baseLine/2)
    
    # print(pointX)
    # print(pointY)
    cl0 = imgHSV[pointY,pointX]
    cl1 = imgHSV[pointY,pointX+splitValue]
    cl2 = imgHSV[pointY,pointX+2*splitValue]
    
    print('[{0},{1},{2}]'.format(cl0[0],cl0[1],cl0[2]))
    print('[{0},{1},{2}]'.format(cl1[0],cl1[1],cl2[2]))
    print('[{0},{1},{2}]'.format(cl2[0],cl1[1],cl2[2]))
    
    
if __name__ == '__main__':
    main()