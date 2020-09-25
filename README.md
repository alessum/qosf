# qosf
Essentially, what the task asks for is to demonstrate that (RX, RY, CZ) is a Universal set, since its able to decompose any basic operator, where these operators creates a Universal set. So, any other operation involving any N number of qubits can be expressed though these $3$ operators.\\

## Short algorithm description
The algorithm we produce is compatible with qiskit. It works as follows.
The terminal, once the algorithm is launched ask for the input file. The file is read a row at a time. Here all its components are found and finally the 'Rewrite\_op' method is called. The method decompose the given operation calling methods that at the end produce a combination of RX, RZ, CNOT gates.

The structure the algorithm is able to recognise is ...[quantum_circuit].[operation]([qubit1], [qubit2 / angle])... that we thought is general enough for the qiskit language. 

## 
