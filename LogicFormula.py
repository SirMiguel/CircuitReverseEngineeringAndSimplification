class LogicFormula:
    def __init__(self):
        pass

    def get_string(self):
        raise NotImplementedError(NotImplemented)

    def get_type(self):
        raise NotImplementedError(NotImplemented)

    def __eq__(self, other):
        return self.get_string() == other.get_string()


class AND(LogicFormula):
    def __init__(self, operands):
        LogicFormula.__init__(self)
        self.operands = operands

    def get_string(self):
        string = self.get_type() + "("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"

    def get_type(self):
        return "AND"

    def __eq__(self, other):
        return self.get_string() == other.get_string()


class XOR(LogicFormula):
    def __init__(self, operands):
        LogicFormula.__init__(self)
        self.operands = operands

    def get_string(self):
        string = self.get_type() + "("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"

    def get_type(self):
        return "XOR"

class NOT(LogicFormula):
    def __init__(self, operand):
        LogicFormula.__init__(self)
        self.operand = operand

    def get_type(self):
        return "NOT"

    def get_string(self):
        string = self.get_type() + "(" + self.operand + ")"
        return string

class OR(LogicFormula):
    def __init__(self, operands):
        LogicFormula.__init__(self)
        self.operands = operands

    def get_type(self):
        return "OR"

    def get_string(self):
        string = self.get_type() + "("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"

class InputVariable(LogicFormula):
    def __init__(self, value):
        LogicFormula.__init__(self)
        self.value = value

    def get_type(self):
        return "InputVariable"

    def get_string(self):
        return str(self.value)