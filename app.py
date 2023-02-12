import numpy as np

X = [[3.0, 1.2, 0.2, -0.4],
     [2.1, 0.6, -0.6, 0.35],
     [1.05, -1, -0.2, -0.6]]

class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
print(3)