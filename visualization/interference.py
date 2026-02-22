import numpy as np

def amplitude_map(state_vector):
    amplitudes = np.abs(state_vector)
    phases = np.angle(state_vector)
    result = []
    for i, (a, p) in enumerate(zip(amplitudes, phases)):
        result.append({
            "state": format(i, f"0{int(np.log2(len(state_vector)))}b"),
            "amplitude": float(a),
            "phase": float(p)
        })
    return result
