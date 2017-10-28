class LogicStatement:
    def __init__(self):
        pass

    def evaluate(self, input):
        raise NotImplementedError(NotImplemented)

    def get_string(self):
        raise NotImplementedError(NotImplemented)


class Variable(LogicStatement):
    def __init__(self, name):
        LogicStatement.__init__(self)
        self.name = name

    def evaluate(self, input):
        return input

    def get_string(self):
        return str(self.name)


class NOT(LogicStatement):
    def __init__(self, operand):
        LogicStatement.__init__(self)
        self.operand = operand
        self.number_of_operands = 1

    def evaluate(self, input):
        return not self.operand.evaluate(input)

    def get_string(self):
        return "NOT(" + self.operand.get_string() + ")"


class AND(LogicStatement):
    def __init__(self, operands):
        LogicStatement.__init__(self)
        self.operands = operands
        self.number_of_operands = 2

    def evaluate(self, input):
        results = []
        for value, operand in zip(input, self.operands):
            results.append(operand.evaluate(value))
        return 0 if 0 in results else 1

    def get_string(self):
        string =  "AND("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"


class OR(LogicStatement):
    def __init__(self, operands):
        LogicStatement.__init__(self)
        self.operands = operands
        self.number_of_operands = 2

    def evaluate(self, input):
        results = []
        for value, operand in zip(input, self.operands):
            results.append(operand.evaluate(value))
        return 1 if 1 in results else 0

    def get_string(self):
        string = "OR("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"


class XOR(LogicStatement):
    def __init__(self, operands):
        LogicStatement.__init__(self)
        self.operands = operands
        self.number_of_operands = 2

    def evaluate(self, input):
        results = []
        for value, operand in zip(input, self.operands):
            results.append(operand.evaluate(value))
        return 1 if (1 in results) and (results.count(1) < len(results)) else 0

    def get_string(self):
        string = "XOR("
        for operand in self.operands[:-1]:
            string += operand.get_string() + ", "
        return string + self.operands[-1].get_string() + ")"