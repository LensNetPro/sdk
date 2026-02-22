from algorithms.grover import GroverSearch
from visualization.interference import amplitude_map

if __name__ == "__main__":
    grover = GroverSearch(n_qubits=3, target_state="101")
    result = grover.run(iterations=2)
    
    print("Measurement Results:")
    print(result)

    print("\nAmplitude Map:")
    print(amplitude_map(grover.qc.state.state))
