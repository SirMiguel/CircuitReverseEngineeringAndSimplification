from LogicFormula import *


class LogicSimplifier:
    def __init__(self, simplifications_strategies):
        self.simplification_strategies = simplifications_strategies

    def simplify(self, formula_to_simplify):
        if not self._is_terminal(formula_to_simplify):
         #   return formula_to_simplify
        #else:
           # for operand_index in range(len(formula_to_simplify.operands)):
           #     formula_to_simplify.operands[operand_index] = self.simplify(formula_to_simplify.operands[operand_index])
            for simpification_strategy in self.simplification_strategies:
                if simpification_strategy.can_apply(formula_to_simplify.get_type()):
                    formula_to_simplify = simpification_strategy.apply(formula_to_simplify)

        #if self._is_terminal(formula_to_simplify):
         #   return formula_to_simplify
        #else:
     #   for operand_index in range(len(formula_to_simplify.operands)):
      #      if not self._is_terminal(formula_to_simplify.operands[operand_index]):
       #         return formula_to_simplify#formula_to_simplify.operands[operand_index] = self.simplify(formula_to_simplify.operands[operand_index])
        #    else:
         #       for simplification_strategy in self.simplification_strategies:
          #          if simplification_strategy.can_apply(formula_to_simplify.operands[operand_index].get_type()):
           #             formula_to_simplify = simplification_strategy.apply(formula_to_simplify.operands[operand_index])
        return formula_to_simplify

    def _is_terminal(self, formula):
        return formula.get_type() == "InputVariable"


class SimplificationStrategy:
    def __init__(self, on_operation_type):
        self.on_operation_type = on_operation_type

    def can_apply(self, formula_type):
        return formula_type == self.on_operation_type

    def apply(self, formula_to_simplify):
        raise NotImplementedError(NotImplemented)

    def _traverse_operands(self, new_operands, formula_to_simplify):
        for operand_index in range(len(formula_to_simplify.operands)):
            #if self._is_terminal(old_operand):
            if formula_to_simplify.operands[operand_index].get_type() == self.on_operation_type:
                new_operands = self._traverse_operands(new_operands, formula_to_simplify.operands[operand_index])
            else:
                 self._apply_operand_simplification(formula_to_simplify.operands[operand_index], new_operands)

        #   new_operands.append(old_operand)
        return new_operands

    def _apply_operand_simplification(self, terminal, new_operands):
        raise NotImplementedError(NotImplemented)

    def _is_terminal(self, operand):
        return operand.get_type() == "InputVariable"

class RemoveRedundantOperations(SimplificationStrategy):
    def __init__(self, on_operation_type):
        SimplificationStrategy.__init__(self, on_operation_type)

    def apply(self, formula_to_simplify):
        raise NotImplementedError(NotImplemented)
        #new_operands = self._traverse_operands(list(), formula_to_simplify)
        #return AND(new_operands) if len(new_operands) > 1 else new_operands[0]

    def _apply_operand_simplification(self, operand, new_operands):
        if self._is_terminal(operand):
            if not self._is_terminal_repeated(operand, new_operands):
                new_operands.append(operand)
        else:
            new_operands.append(operand)

    def _is_terminal_repeated(self, terminal, operands):
        for new_operand in operands:
            if new_operand == terminal:
                return True
        return False


class RemoveRedundantANDs(RemoveRedundantOperations):
    def __init__(self):
        RemoveRedundantOperations.__init__(self, "AND")

    def apply(self, formula_to_simplify):
        new_operands = self._traverse_operands(list(), formula_to_simplify)
        return AND(new_operands) if len(new_operands) > 1 else new_operands[0]

class RemoveRedundantORs(RemoveRedundantOperations):
    def __init__(self):
        RemoveRedundantOperations.__init__(self, "OR")

    def apply(self, formula_to_simplify):
        new_operands = self._traverse_operands(list(), formula_to_simplify)
        return OR(new_operands) if len(new_operands) > 1 else new_operands[0]

class RemoveOperandRepeatedInside(SimplificationStrategy):
    def __init__(self):
        SimplificationStrategy.__init__(self, "AND")

    def apply(self, formula_to_simplify):
        pass
        #new_operands = self._traverse_operands(list(), formula_to_simplify)


    def _apply_operand_simplification(self, terminal, new_operands):
        pass
       # if terminal
        #new_operands = []
        #for operand in formula_to_simplify.operands:
         #   if not self._is_terminal(operand):
          #      new_operands.append(operand)
           # else:
            #    if operand.get_type() in ["AND", "OR"]:
             #       self._traverse_operands(new_operands, operand)


        #new_formula = self._apply_terminal_condition()
#class RemoveUncess
        # def _get_new_operands(self, operands, formula_to_simplify):
        #   for old_operand in formula_to_simplify.operands:
        #      repeated = False
        #     if old_operand.get_type() == "InputVariable":
        #        for new_operand in operands:
        #           if new_operand == old_operand:
        #              repeated = True
        #     if not repeated:
        #         operands.append(old_operand)
        # elif old_operand.get_type() == "AND":
        #   operands = self._get_new_operands(operands, old_operand)
        # else:
        #   operands.append(old_operand)
        # return operands