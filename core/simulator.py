from .circuit import QuantumCircuit
from .gate import hadamard

def create_superposition(n_qubits):
    qc = QuantumCircuit(n_qubits)
    for i in range(n_qubits):
        qc.apply_single_qubit_gate(hadamard(), i)
    return qc
