import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time


X = pickle.load(open("X_Ronny.pickle", "rb")) #Dessa tror jag är ett objekt med preppade bilder
y = pickle.load(open("y_Ronny.pickle", "rb")) #Denna är svaret på vad bilderna är
X = X/255.0

dense_layers = [0]
layer_sizes = [64]
conv_layers =[3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
            tensorboard = TensorBoard(log_dir='logs\{}'.format(NAME))
            print(NAME)
            model = Sequential()

            model.add(Conv2D(layer_size, (3,3), input_shape = X.shape[1:])  )
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2,2)))

            for l in range(conv_layer - 1):
                model.add(Conv2D(layer_size, (3,3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2,2)))

            model.add(Flatten())
            for l in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation("relu"))

            model.add(Dense(64))
            model.add(Activation("relu"))

            model.add(Dense(3, activation=tf.nn.softmax))

            #model.add(Dense(2))
            #model.add(Activation('sigmoid'))

            model.compile(loss="sparse_categorical_crossentropy",
                          optimizer="adam",
                          metrics=['accuracy'])
            print("oh yeah, almost there")


            model.fit(X, y, batch_size=32, epochs=20, validation_split=0.1, callbacks=[tensorboard])

            #model.save_weights('./checkpoints/my_checkpoint')

            #model.save('my_model.h5')

model.save('RonnyLearn.model')
model.summary()


#model.save_weights('./checkpoints/my_checkpoint')


#Ev behöver jag inte spara modellen, då den görs så snabbt.
            # Run the operation by feeding input
            #saver = tf.train.Saver()
            #sess = tf.Session()
            # Now, save the graph
            #saver.save(sess, 'C:/NN')
            #saver.save(tf.Session(), 'C:/Ronny', global_step=10)


#Fråm cmd: tensorboard --logdir=logs/ --host localhost --port 8088
#I browser http://localhost:8088








