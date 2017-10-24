from LogicFormula import *


class LogicSimplifier:
    def __init__(self, simplifications_strategies):
        self.simplification_strategies = simplifications_strategies

    def simplify(self, formula_to_simplify):
        if not self._is_terminal(formula_to_simplify):
            for simpification_strategy in self.simplification_strategies:
                if simpification_strategy.can_apply(formula_to_simplify.get_type()):
                    formula_to_simplify = simpification_strategy.apply(formula_to_simplify)
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
        for operand in formula_to_simplify.operands:
            if operand.get_type() == self.on_operation_type:
                new_operands = self._traverse_operands(new_operands, operand)
            else:
                 self._apply_operand_simplification(operand, new_operands)
        return new_operands

    def _apply_operand_simplification(self, old_operand, new_operands):
        raise NotImplementedError(NotImplemented)

    def _is_terminal(self, operand):
        return operand.get_type() == "InputVariable"


class RemoveRedundantOperations(SimplificationStrategy):
    def __init__(self, on_operation_type):
        SimplificationStrategy.__init__(self, on_operation_type)

    def apply(self, formula_to_simplify):
        raise NotImplementedError(NotImplemented)

    def _apply_operand_simplification(self, old_operand, new_operands):
        if self._is_terminal(old_operand):
            if not self._is_terminal_repeated(old_operand, new_operands):
                new_operands.append(old_operand)
        else:
            new_operands.append(old_operand)

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
        new_operands = self._traverse_operands(formula_to_simplify.operands, formula_to_simplify)
        return AND(new_operands)

    def _apply_operand_simplification(self, old_operand, new_operands):
        if old_operand.get_type() == "OR":
            for or_operand in old_operand.operands:
                if self.is_outside_of_or(or_operand, new_operands):
                    new_operands.remove(old_operand)

    def is_outside_of_or(self, operand, containing_and_operands):
        for containing_and_operand in containing_and_operands:
            if operand == containing_and_operand:
                return True
        return False
