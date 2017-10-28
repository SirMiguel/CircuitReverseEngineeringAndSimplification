import atpy

class LogicIO:
    def __init__(self, number_of_inputs, number_of_outputs):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs

    def open_logic_dataset(self, filename, location):
        dataset_table = atpy.Table(location + "/" + filename, type="ascii")

        output_dictionary = dict()
        input_dictionary = dict()
        for key, key_index in zip(dataset_table.columns.keys, range(len(dataset_table.columns))):
            key_values = []
            for row in range(len(dataset_table)):
                key_values.append(dataset_table[row][key_index])

            if key_index < self.number_of_inputs:
                input_dictionary.update({key : key_values})
            else:
                output_dictionary.update({key : key_values})

        dataset_dictionary = {
            "inputs" : input_dictionary,
            "outputs" : output_dictionary
        }

        return dataset_dictionary

    '''  circuits = dict()
           for output in range(self.number_of_outputs):
               full_circuit_operands = []
               for row in range(len(dataset_table)):
                   circuit_output = dataset_table[row][output + self.number_of_inputs]
                   and_operands = []
                   for column in range(len(dataset_table.columns) - self.number_of_outputs):
                       input_variable_value = dataset_table[row][column]
                       if circuit_output == 1:
                           if input_variable_value == 1:
                               and_operands.append(InputVariable(dataset_table.keys()[column]))
                           else:
                               and_operands.append(NOT(InputVariable(dataset_table.keys()[column])))
                       else:
                           if input_variable_value == 1:
                               and_operands.append(InputVariable(dataset_table.keys()[column]))
                           else:
                               and_operands.append(InputVariable(dataset_table.keys()[column]))
                   full_circuit_operands.append(AND(and_operands))
               circuits.update({dataset_table.keys()[self.number_of_inputs + output] : OR(full_circuit_operands)})
          '''


