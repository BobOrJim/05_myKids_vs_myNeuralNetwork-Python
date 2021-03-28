import cv2
import tensorflow as tf

CATEGORIES = ["pase", "sax", "sten"]

def prepare(filepath):
    IMG_SIZE = 50;
    img_array =cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255


model = tf.keras.models.load_model("RonnyLearn.model")

#prediction = model.predict([prepare('PASE.jpg')])
#print(prediction)
#prediction = model.predict([prepare('SAX.jpg')])
#print(prediction)
#prediction = model.predict([prepare('SAX.jpg')])
#print(prediction)
#prediction = model.predict([prepare('PASE2.jpg')])
#print(prediction)

#CATEGORIES = ["pase", "sax", "sten"]


from datetime import datetime #Vad är skillnaden på denna rad gentemot #import datetime
cv2.namedWindow("My_preview")
vc = cv2.VideoCapture(0)

#Att testa
vc.set(3, 2280)
vc.set(3, 1720)



if vc.isOpened(): #try to get the first frame
    rval, frame = vc.read() #This bugger returns a tuple.
else:
    rval = False

prediction = model.predict([prepare('C:/Ronny/testNow.jpg')])
print(prediction[0])
myStringPASE = ""
myStringSAX = ""
myStringSTEN = ""
myStringMyVal = ""
myStringTot = ""
from time import sleep # kanske till framtiden.

#from PIL import Image
#im = Image.open('C:/Users/jimmy/PycharmProjects/test2/CoolDude.jpg')
#im.thumbnail((500, 500), Image.ANTIALIAS)
#im.show()
#im.rotate(45).show()
#im.close()

n = 0
img = cv2.imread('C:/Users/jimmy/PycharmProjects/test2/CoolDude4.jpg')
while rval:

    cv2.imshow("HEEERRRREEESSS RONNY", img)
    rval, frame = vc.read()
    #cv2.imshow("HEEERRRREEESSS RONNY", frame)# wokring orgiginal
    key = cv2.waitKey(20)
    n = n + 1
    #print(n)
    if n == 20:         #key == 97: #a
        print("då")
        cv2.imwrite('C:/Ronny/testNow.jpg', frame)
        prediction = model.predict([prepare('C:/Ronny/testNow.jpg')])
        myStringPASE = str(prediction[0][0])
        myStringSAX = str(prediction[0][1])
        myStringSTEN = str(prediction[0][2])
    if key == 27: # exit on ESC
        break
    print("Hej")
    cv2.putText(frame, myStringPASE, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    cv2.putText(frame, myStringSAX, (200, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    cv2.putText(frame, myStringSTEN, (200, 280), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    if n == 25: #key == 32: # choose sign on space
        if (prediction[0][0] > prediction[0][1]) and (prediction[0][0] > prediction[0][2]):
            img = cv2.imread('C:/Users/jimmy/PycharmProjects/test2/CoolDude4_Sax.jpg')
            print("Nova har valt PÅSE, Ronny väljer SAX")
            #sleep(3)
        if (prediction[0][1] > prediction[0][0]) and (prediction[0][1] > prediction[0][2]):
            img = cv2.imread('C:/Users/jimmy/PycharmProjects/test2/CoolDude4_Sten.jpg')
            print("Nova har valt SAX, Ronny väljer STEN")
            #sleep(3)
        if (prediction[0][2] > prediction[0][0]) and (prediction[0][2] > prediction[0][1]):
            img = cv2.imread('C:/Users/jimmy/PycharmProjects/test2/CoolDude4_Pase.jpg')
            print("Nova har valt STEN, Ronny väljer PÅSE")
            #sleep(3)
    if n == 37:
        img = cv2.imread('C:/Users/jimmy/PycharmProjects/test2/CoolDude4.jpg')
        n = 0

    #cv2.putText(frame, myStringSTEN, (200, 280), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))


vc.release()
cv2.destroyWindow("preview")



