from LogicIO import *
from LogicStatement import *
from os import getcwd
from itertools import combinations_with_replacement, permutations, combinations

def does_circuit_give_expected_output(circuit_to_test, inputs_to_test, expected_outputs):
    for input_row, expected_output in zip(inputs_to_test, expected_outputs):
        if circuit_to_test.evaluate(input_row) != expected_output:
            return False
    return True

def get_inputs_for_variables(input_variables_to_get, circuit_inputs):
        inputs = []
        for input_row in range(len(circuit_inputs[input_variables_to_get[0]])):
            row = []
            for input_name in input_variables_to_get:
                row.append(circuit_inputs[input_name][input_row])
            inputs.append(row)
        return inputs


def get_inputs(circuits_inputs, circuit_to_get_inputs_for):
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


'''

def thingy(circuits_inputs, circuits_with_outputs, max_possible_operands, circuit_operations):
    found_circuits = dict()
    for number_of_operands in range(max_possible_operands):
        #circuit_not_found = True
        operations_repo = []
        for candidate_variables in combinations_with_replacement(circuits_inputs.keys(), number_of_operands + 1):
            for circuit_operation in circuit_operations:
                potential_operands = operations_repo + list(candidate_variables)
                for operand_combination in permutations(potential_operands, number_of_operands):
                    operations_repo.append(circuit_operation(operand_combination))


            for candidate_circuit in operations_repo:
                for circuit_name, circuit_outputs in circuits_with_outputs.items():
                    if does_circuit_give_expected_output(candidate_circuit,
                                                         get_inputs_for_variables(candidate_variables, circuits_inputs),
                                                         circuit_outputs):
                        found_circuits.update({circuit_name: candidate_circuit})
                        #circuit_not_found = False
    return found_circuits
'''




test_data = LogicIO(8, 8).open_logic_dataset("ReverseEngineeringDataset.txt", getcwd())

circuits_inputs = test_data["inputs"]
circuits_outputs = test_data["outputs"]

#found_circuits = dict()

#variables = circuits_inputs.keys()
variables = [Variable(input_name) for input_name in circuits_inputs.keys()]
circuit_operations = [OR, AND, NOT, XOR]

all_possible_variables_combinations = []
#max_number_of_variables_used = 3
found_circuits = dict()
#for number_of_variables_to_combine in range(max_number_of_variables_used):
 #   number_of_variables_to_combine += 1
  #  all_possible_variables_combinations.extend(permutations(variables, number_of_variables_to_combine))


# for candidate_circuit in circuits_to_try:
# print("candidate circuit", candidate_circuit.get_string())
all_possible_circuits = variables.copy()
circuits_still_to_get = circuits_outputs.copy()
circuits_tried = []
circuits_to_try = variables.copy()
while len(found_circuits) < len(circuits_outputs.keys()):
    while circuits_to_try:
        candidate_circuit = circuits_to_try.pop()
        #print(candidate_circuit.get_string())

        for circuit_name, circuit_outputs in circuits_still_to_get.copy().items():
            if does_circuit_give_expected_output(candidate_circuit, get_inputs(circuits_inputs, candidate_circuit), circuit_outputs):
                found_circuits.update({circuit_name : candidate_circuit})
                print("----------------------------------------")
                print("Candidate found")
                print(circuit_name, candidate_circuit.get_string())
                print("----------------------------------------")
                del circuits_still_to_get[circuit_name]
        circuits_tried.append(candidate_circuit)

    circuits_to_try.extend([XOR(list(permutation)) for permutation in permutations(circuits_tried, 2)])
    circuits_to_try.extend([AND(list(permutation)) for permutation in permutations(circuits_tried, 2)])
    circuits_to_try.extend([OR(list(permutation)) for permutation in permutations(circuits_tried, 2)])
    circuits_to_try.extend([NOT(permutation[0]) for permutation in permutations(circuits_tried, 1)])


print("done")

for circuit_name, circuit_logic in found_circuits.items():
    print(circuit_name, circuit_logic.get_string())