from flask import Flask, request, jsonify
from algorithms.grover import GroverSearch

app = Flask(__name__)

@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    algo = data.get("algorithm")
    
    if algo == "grover":
        n = data.get("qubits", 2)
        target = data.get("target", "01")
        iterations = data.get("iterations", 1)
        grover = GroverSearch(n, target)
        result = grover.run(iterations=iterations)
        return jsonify(result)
    
    return jsonify({"error": "Unsupported algorithm"}), 400

if __name__ == "__main__":
    app.run(debug=True)
