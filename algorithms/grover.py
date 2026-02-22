import numpy as np
from core.circuit import QuantumCircuit
from core.gate import hadamard, identity, kron_n

class GroverSearch:
    def __init__(self, n_qubits, target_state):
        self.n_qubits = n_qubits
        self.target_index = int(target_state, 2)
        self.qc = QuantumCircuit(n_qubits)
        for i in range(n_qubits):
            self.qc.apply_single_qubit_gate(hadamard(), i)

    def oracle(self):
        dim = 2 ** self.n_qubits
        oracle = np.eye(dim)
        oracle[self.target_index, self.target_index] = -1
        return oracle

    def diffusion(self):
        dim = 2 ** self.n_qubits
        s = np.ones((dim, dim)) / dim
        return 2 * s - np.eye(dim)

    def run(self, iterations=1, shots=1024):
        for _ in range(iterations):
            self.qc.state.apply_operator(self.oracle())
            self.qc.state.apply_operator(self.diffusion())
        return self.qc.run(shots)
