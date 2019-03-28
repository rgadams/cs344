import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
import numpy as np

class LogicGateModel:
    '''This class models a two-input logic gate function, i.e., AND, OR, XOR, NAND, NOR, XNOR
    hidden_layers gives a list of layer specifications of the form: (#ofNodes, activationFunction);
    output_layer is similar but with only layer specification.
    '''

    def __init__(self,
                 optimizer=Adam(lr=0.1),
                 hidden_layers=[],
                 output_layer=(1, tf.keras.activations.linear),
                 loss_function=tf.keras.losses.mse
                 ):
        self.model = Sequential()
        for layer in hidden_layers:
            self.model.add(Dense(layer[0], input_dim=2, activation=layer[1]))
        self.model.add(Dense(output_layer[0], input_dim=2, activation=output_layer[1]))
        self.model.compile(loss=loss_function,
                           optimizer=optimizer,
                           metrics=[tf.keras.metrics.binary_accuracy]
                           )

    def train(self, X, y, n_epochs=100):
        self.model.fit(X, y, batch_size=1, epochs=n_epochs, verbose=0)

    def predict(self, X):
        return self.model.predict(X)


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([[0], [1], [1], [0]])
model = LogicGateModel(
    hidden_layers=[(3, tf.keras.activations.tanh)],
    output_layer=(1, tf.nn.sigmoid),
    loss_function=tf.keras.losses.binary_crossentropy
)
model.train(X, y_xor, n_epochs=1000)
print(model.predict(X))

'''
I tried many things to simplify the network, but most things failed. I tried changing the activation function of the 
output layer and surprisingly only the sigmoid function worked. Tanh and relu did not. The one thing that did work was 
reducing the number of nodes in the hidden layer. I was able to reduce it to three, but two seemed to lose too much 
information to get the correct answer. I also tried changing the optimizer, which I guess is not really simplification.
The important thing to note is that there is not much more simplification that can be done here. We only have one hidden
layer so the complexity was not very high to begin with.
'''