# https://medium.freecodecamp.org/building-a-3-layer-neural-network-from-scratch-99239c4af5d3
import pandas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import sklearn
import sklearn.datasets
import sklearn.linear_model
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

np.random.seed(0)


# This is the forward propagation function
def forward_prop(model, a0):
    # Load parameters from model
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'], model['b3']

    # Do the first Linear step
    z1 = a0.dot(W1) + b1

    # Put it through the first activation function
    a1 = np.tanh(z1)

    # Second linear step
    z2 = a1.dot(W2) + b2

    # Put through second activation function
    a2 = np.tanh(z2)

    # Third linear step
    z3 = a2.dot(W3) + b3

    # For the Third linear activation function we use the softmax function
    a3 = softmax(z3)

    # Store all results in these values
    cache = {'a0': a0, 'z1': z1, 'a1': a1, 'z2': z2, 'a2': a2, 'a3': a3, 'z3': z3}
    return cache
