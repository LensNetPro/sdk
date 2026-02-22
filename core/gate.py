import numpy as np

def hadamard():
    return (1/np.sqrt(2)) * np.array([[1, 1],
                                      [1, -1]])

def pauli_x():
    return np.array([[0, 1],
                     [1, 0]])

def identity():
    return np.eye(2)

def kron_n(gates):
    result = gates[0]
    for g in gates[1:]:
        result = np.kron(result, g)
    return result
