import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "C:/Ronny/Hands"
CATEGORIES = ["pase", "sax", "sten"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap='gray')
        #plt.show()
        print(category)
        print(img)
        #break
    #break

##Section 2
IMG_SIZE = 50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
#plt.show()

##Section 3
training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                print(" found crap ")
                pass


print(" Startar_training data finktionen ")

create_training_data()
print("Har just kört create_training_data() ")
print(len(training_data))


#Sektion 4
import random
random.shuffle(training_data)

print(training_data[1])
print(training_data[2])
print(training_data[3])
print(training_data[4])

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) #Etta på sluten är för att det är grayscale

#Sektion 5: För att spara min data innan jag börjar bomba in skiten i modellen
import pickle
pickle_out = open("X_Ronny.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y_Ronny.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
print("DONE!!!! att fixa till indata")

