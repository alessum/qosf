# qosf
Essentially, what the task asks for is to demonstrate that (RX, RY, CZ) is a Universal set, since its able to decompose any basic operator (I,H, X, Y, Z, RX, RY, RZ, CX, CZ). Amongst these we identify a Universal set: H, RZ, CNOT. So, any other operation involving any N number of qubits can be expressed though these 3 operators.\\

## Short algorithm description
The algorithm we produce is compatible with qiskit. It works as follows.
The terminal, once the algorithm is launched ask for the input file. The file is read a row at a time. Here all its components are found and finally the 'Rewrite\_op' method is called. The method decompose the given operation calling methods that at the end produce a combination of RX, RZ, CNOT gates.

The structure the algorithm is able to recognise is ...[quantum_circuit].[operation]([qubit1], [qubit2 / angle])... that we thought is general enough for the qiskit language. 

## Analysis
Talking about the overhead that the conversion causes we can start by seeing that, considering our nine basic gates, on average the post-coversion gates are increased by 78%. On the other hand the number of different gates in one third.
Anyway, we see there are some simple ways to optimise the number of gates just by looking at couple of consecutive matrices.
Firstly, one could use the Pauli identities like sigma^2=id (working for all the three even if Y decomposes in two gates). 
Also, one could remove the RZ(0) and annihilate the couples like RZ(alpha)RZ(-alpha). In fact RZ and RX are defined as the exponentiation of a Pauli matrix times i*alpha.  
In this way a couple of RY(alpha) would correctly become RZ(pi/2)RX(alpha)RX(alpha)RZ(-pi/2) = RZ(pi/2)RX(2*alpha)RZ(-pi/2).
We observe that some gates are decomposed up to a global phase (for instance Y=exp(i pi/2)*RX(pi)*RZ(-pi)). Nevertheless, as we know in quantum programming it can be ignored since it is physically meaningless. 
