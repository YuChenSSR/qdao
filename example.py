from qdao import Engine
from qiskit.circuit.random import random_circuit
from qiskit import transpile
from qiskit_aer import Aer

# Create a qiskit quantum circuit `circ`
circ = random_circuit(28, 20, measure=False)
backend = Aer.get_backend("aer_simulator")
circ = transpile(circ, backend=backend)

# `num_primary`: size of a compute unit
# `num_local`: size of a storage unit
eng = Engine(circuit=circ, num_primary=26, num_local=22)
eng.run()
