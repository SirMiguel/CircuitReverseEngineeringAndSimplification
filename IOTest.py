from LogicIO import LogicIO
from os import getcwd
from LogicStatement import *
from itertools import permutations, combinations_with_replacement

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



#for each combination of variables
    #for each possible circuit with those variables
        #try itself as a candidate circuit
            #for circuit_outputs in ciruits_outputs
                #try the circuit against its outputs
                    #if it works return
            #if no circuit found try again adding another variable to the mix

def thingy(citcuits_inputs, circuits_with_outputs, max_possible_operands, circuit_operations):
    found_circuits = dict()
    for number_of_operands in range(max_possible_operands):
        #circuit_not_found = True
        operations_repo = []
        for candidate_variables in combinations_with_replacement(circuits_inputs.keys(), number_of_operands + 1):
            for circuit_operation in circuit_operations:
                potential_operands = operations_repo + list(candidate_variables)
               # if circuit_operation.number_of_operands >= len(candidate_variables):
                for operand_combination in permutations(potential_operands, number_of_operands):
                    operations_repo.append(circuit_operation(operand_combination))


            for candidate_circuit in operations_repo:
                for circuit_name, circuit_outputs in circuits_outputs.items():
                    if does_circuit_give_expected_output(candidate_circuit,
                                                         get_inputs_for_variables(candidate_variables, circuits_inputs),
                                                         circuit_outputs):
                        found_circuits.update({circuit_name: candidate_circuit})
                        #circuit_not_found = False
    return found_circuits

#def get_all_circuits(number_of_circuits, circuits_with_outputs, input_variables_with_input_combinations):
#    circuits_found = dict()

   # while len(circuits_found) < number_of_circuits:


#def do_thing(variables, i, current_candidate_variables, current_circuit, circuits_outputs):
    #found_circuits = dict()
    #for variable_name in variables.keys():
 #   circuit_not_found = True
  #  for circuit_name, circuit_outputs in circuits_outputs.items():
   #     if does_circuit_give_expected_output(current_circuit, get_inputs_for_variables(candidate_variables, circuits_inputs), circuit_outputs):
    #        found_circuits.update({circuit_name : candidate_circuit})
     #       circuit_not_found = False
        #return do_thing(variables, i+1,current_candidate_variables.append(variables[i], current_circuit, circuits_outputs)
        #return current_circuit



#for variable_name in circuits_inputs.keys():
 #   candidate_circuit = NOT(Variable(variable_name))
  #  found_circuit = False
   # for circuit_name, circuit_outputs in circuits_outputs.items():#zip(circuits_outputs.keys(), circuits_outputs.values()):
    #    if does_circuit_give_expected_output(candidate_circuit, circuits_inputs[variable_name], circuit_outputs):
     #       found_circuits.update({circuit_name : candidate_circuit})
      #      found_circuit = True

   # if not found_circuit:
    #    for variable_2_name in circuits_inputs.keys():
     #       candidate_variables = [variable_name, variable_2_name]
      #      if variable_name != variable_2_name:
       #         candidate_circuit = XOR([Variable(variable_name), Variable(variable_2_name)])
        #        for circuit_name in circuits_outputs.keys():

         #           if does_circuit_give_expected_output(candidate_circuit, get_inputs_for_variables(candidate_variables, circuits_inputs), circuits_outputs[circuit_name]):
          #              found_circuits.update({circuit_name: candidate_circuit})

#for circuit_name, circuit in found_circuits.items():
 #   print(circuit_name, circuit.get_string())
'''
from LogicIO import LogicIO
from os import getcwd

test_data = LogicIO(8, 8).open_logic_dataset("ReverseEngineeringDataset.txt", getcwd())
circuit_two = test_data["outputs"]
print(circuit_two)
'''



test_data = LogicIO(8, 8).open_logic_dataset("ReverseEngineeringDataset.txt", getcwd())

circuits_inputs = test_data["inputs"]
circuits_outputs = test_data["outputs"]

#found_circuits = dict()

#variables = circuits_inputs.keys()
variables = [Variable(input_name) for input_name in circuits_inputs.keys()]
circuit_operations = [OR, AND, NOT, XOR]


found_circuits = thingy(circuits_inputs, circuits_outputs, 3, circuit_operations)
print(found_circuits)