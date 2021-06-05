import numpy as np
import keras
from keras import layers
from keras.optimizers import Adam
from keras.models import Model


def getAutoencoder(input_size):
    inputs = keras.Input(input_size)
    x = layers.Conv2D(64, 3, activation="relu", padding="same")(inputs)
    x = layers.MaxPooling2D((2,2), padding="same")(x)
    x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
    x = layers.MaxPooling2D((2,2), padding="same")(x)

    x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
    x = layers.UpSampling2D((2,2))(x)
    x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
    x = layers.UpSampling2D((2,2))(x)
    finished = layers.Conv2D(1, (3,3), activation="sigmoid", padding="same")(x)

    autoencoder = keras.Model(inputs, finished)
    autoencoder.compile(optimizer=Adam(lr = 1e-4), loss='binary_crossentropy', metrics=['accuracy'])

    autoencoder.summary()
    return autoencoder


def getEmbedder(model, i, optimizer):
    emb = Model(inputs = model.layers[0].input, outputs=model.layers[i-1].output)
    emb.summary()
    emb.compile(loss="mean_squared_error", optimizer=optimizer)
    return emb

def pretrain(model, input_size, X_data):
    print("Pretraining")
    for i in range(1, len(model.layers)):
        if not isinstance(model.layers[i], layers.Conv2D):
            print("Skipping layer {}, because it is not a Conv2Dlayer".format(type(model.layers[i])))
            continue
        embedder = getEmbedder(model, i, optimizer=Adam(lr = 1e-4))
        current_data = embedder.predict(X_data)
        noisy_data = current_data + 0.1 + np.random.normal(loc=0, scale=1, size=current_data.shape)

        inputs = keras.Input(shape=(current_data.shape[1], ))
        x = getAutoencoder(model.layers[i].output_shape)(inputs)
        dae = Model(inputs=inputs, outputs=x)
        dae.summary()
        dae.compile(loss="mean_squared_error", optimizer=Adam(lr=1e-4))
        dae.fit(
                noisy_data,
                current_data,
                batch_size=2,
                epochs=50,
                verbose=1,
                validation_split=0.3,
                )
        model.layers[i].set_weights(dae.layers[1].get_weights()[:2])
        model.layers[i].trainable = False
    model.save_weights('pretrained_layer_weights')



