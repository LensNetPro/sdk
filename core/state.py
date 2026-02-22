import numpy as np

class QuantumState:
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits
        self.dim = 2 ** n_qubits
        self.state = np.zeros(self.dim, dtype=complex)
        self.state[0] = 1.0  # |00...0>

    def apply_operator(self, operator: np.ndarray):
        self.state = operator @ self.state

    def measure(self, shots=1024):
        probabilities = np.abs(self.state) ** 2
        outcomes = np.random.choice(self.dim, shots, p=probabilities)
        counts = {}
        for o in outcomes:
            bitstring = format(o, f"0{self.n_qubits}b")
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts
