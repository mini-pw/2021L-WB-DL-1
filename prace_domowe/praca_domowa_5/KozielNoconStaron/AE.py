import keras
from keras import layers

def buildModel():
  input_img = keras.Input(shape=(224, 224, 3), name='INPUT')

  x = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
  x = layers.MaxPooling2D((2, 2), padding='same')(x)
  x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
  x = layers.MaxPooling2D((2, 2), padding='same')(x)
  x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)

  encoded = layers.MaxPooling2D((2, 2), padding='same', name ="CODE")(x)



  x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
  x = layers.UpSampling2D((2, 2))(x)
  x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
  x = layers.UpSampling2D((2, 2))(x)
  x = layers.Conv2D(16, (3, 3), activation='relu',padding = "same")(x)
  x = layers.UpSampling2D((2, 2))(x)
  decoded = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same', name ="OUTPUT")(x)

  autoencoder = keras.Model(input_img, decoded)
  return autoencoder

  
