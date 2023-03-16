import qiskit

qc = QauntumCircuit(5)

for i in range(3):
    qc.x(0);qc.h(0)
vizualize_transition(qc, trace = True)