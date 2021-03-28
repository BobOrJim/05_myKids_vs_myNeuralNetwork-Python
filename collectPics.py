import cv2
from datetime import datetime #Vad är skillnaden på denna rad gentemot #import datetime
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    myString = str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour)
    myString2 = str(datetime.now().minute) + str(datetime.now().second)
    myString3 = 'C:/Ronny/'
    if key == 97: #a
        myFileName = myString3 + "STEN_" + myString + myString2 + ".jpg"
        print(myFileName)
        cv2.imwrite(myFileName, frame)
    if key == 98: #B
        myFileName = myString3 + "SAX_" + myString + myString2 + ".jpg"
        print(myFileName)
        cv2.imwrite(myFileName, frame)
    if key == 99: #c
        myFileName = myString3 + "PASE_" + myString + myString2 + ".jpg"
        print(myFileName)
        cv2.imwrite(myFileName, frame)
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("preview")
