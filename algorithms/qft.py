import numpy as np
from core.circuit import QuantumCircuit

class QFT:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits
        self.qc = QuantumCircuit(n_qubits)

    def qft_matrix(self):
        dim = 2 ** self.n_qubits
        omega = np.exp(2j * np.pi / dim)
        matrix = np.zeros((dim, dim), dtype=complex)
        for x in range(dim):
            for y in range(dim):
                matrix[x, y] = omega ** (x * y)
        return matrix / np.sqrt(dim)

    def run(self, shots=1024):
        operator = self.qft_matrix()
        self.qc.state.apply_operator(operator)
        return self.qc.run(shots)
