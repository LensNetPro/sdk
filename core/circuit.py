import numpy as np
from .state import QuantumState
from .gate import identity, kron_n

class QuantumCircuit:
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits
        self.state = QuantumState(n_qubits)

    def apply_single_qubit_gate(self, gate, target):
        gates = []
        for i in range(self.n_qubits):
            gates.append(gate if i == target else identity())
        operator = kron_n(gates)
        self.state.apply_operator(operator)

    def run(self, shots=1024):
        return self.state.measure(shots)
