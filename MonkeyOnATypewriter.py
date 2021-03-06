from LogicIO import *
from LogicStatement import *
from os import getcwd, linesep
from itertools import combinations

def get_number_of_operations(circuit):
    if isinstance(circuit, Variable):
        return 0
    elif isinstance(circuit, NOT):
        return get_number_of_operations(circuit.operand) + 1
    else:
        number_of_operations_in_operand = 0
        for operand in circuit.operands:
            number_of_operations_in_operand += get_number_of_operations(operand) + 1
        return number_of_operations_in_operand

def does_circuit_give_expected_output(circuit_to_test, inputs_to_test, expected_outputs):
    # This method tests each input vector against each expected output for the circuit being tested
    # If false this indicates that the circuits are not a match
    # If true this indicates a found circuit
    for input_row, expected_output in zip(inputs_to_test, expected_outputs):
        if circuit_to_test.evaluate(input_row) != expected_output:
            return False
    return True


def get_inputs(circuits_inputs, circuit_to_get_inputs_for):
    #This method recursively finds all the inputs for the operands,
    # traversing until it reaches the end variables at each operand
    if isinstance(circuit_to_get_inputs_for, Variable):
        return circuits_inputs[circuit_to_get_inputs_for.name]
    elif isinstance(circuit_to_get_inputs_for, NOT):
        return get_inputs(circuits_inputs, circuit_to_get_inputs_for.operand)
    else:
        operand_inputs = []
        for operand in circuit_to_get_inputs_for.operands:
            operand_inputs.append(get_inputs(circuits_inputs, operand))
        fixed_operand_inputs = []
        for row_index in range(len(operand_inputs[0])):
            row = []
            for column_index in range(len(operand_inputs)):
                row.append(operand_inputs[column_index][row_index])
            fixed_operand_inputs.append(row)
        return fixed_operand_inputs

test_data = LogicIO(8, 8).open_logic_dataset("ReverseEngineeringDataset.txt", getcwd())

circuits_inputs = test_data["inputs"]
circuits_outputs = test_data["outputs"]

# Initial circuits to try are the simplest
variables = [Variable(input_name) for input_name in circuits_inputs.keys()]
circuits_to_try = set(variables.copy())
circuits_to_try = circuits_to_try.union([NOT(variable) for variable in variables])

found_circuits = dict()
circuits_tried = set()



while len(found_circuits.copy().keys()) < len(circuits_outputs.keys()):
    #circuits to try are sorted by the length of the boolean statement
    # as a string, this ensures that the simplest circuits are chosen
    circuits_to_try = set(sorted(circuits_to_try, key=lambda circuit : get_number_of_operations(circuit)))
    print("Number of circuits to try:", len(circuits_to_try))

    while circuits_to_try:
        candidate_circuit = circuits_to_try.pop()
        for circuit_name, circuit_outputs in circuits_outputs.items():
            if does_circuit_give_expected_output(candidate_circuit, get_inputs(circuits_inputs, candidate_circuit), circuit_outputs):
                if circuit_name in found_circuits.keys():
                    if get_number_of_operations(found_circuits[circuit_name]) > get_number_of_operations(candidate_circuit):
                        found_circuits.update({circuit_name : candidate_circuit})
                        print("Simpler circuit found")
                        print(circuit_name, candidate_circuit.get_string())
                        # This allows a simpler circuit solution to a given output to be given while we are still
                        # trying to find a solution to all circuit outputs
                else:
                    found_circuits.update({circuit_name : candidate_circuit})
                    print("Circuit found")
                    print(circuit_name, candidate_circuit.get_string())
        circuits_tried.add(candidate_circuit)

    # Next generation of circuits to try
    # This simply adds in different combinations of circuits already tried to the list of
    # new circuits to try, making sure to not add duplicates
    if len(found_circuits.copy().keys()) < len(circuits_outputs.keys()):
        for tried_circuit in circuits_tried:
            # Avoids adding double negatives
            # Assumed due to the specification that the circuit is as simple as possible
            if not isinstance(tried_circuit, NOT):
                circuits_to_try.add(NOT(tried_circuit))

        combinations_of_two_operands =  combinations(circuits_tried, 2)
        for combination_of_two_operands in combinations_of_two_operands:
            combination_of_two_operands = list(combination_of_two_operands)
            circuits_to_try.add(XOR(combination_of_two_operands))
            circuits_to_try.add(OR(combination_of_two_operands))
            circuits_to_try.add(AND(combination_of_two_operands))

print("done")

for circuit_name, circuit_logic in sorted(found_circuits.items()):
    print(circuit_name, circuit_logic.get_string())

# Outputs the found circuits in the right order on separated lines
output_strings = [circuit.get_string() for circuit_name, circuit in sorted(found_circuits.items())]
with open(getcwd() + "/circuits.txt", "w") as file:
    for output_line in output_strings:
        file.write(output_line + linesep)