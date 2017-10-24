from LogicFormula import *
from LogicSimplifier import *

logic_statement = AND([InputVariable("A"), OR([InputVariable("L"), InputVariable("Q")]), InputVariable("A"), AND([InputVariable("A"), InputVariable("D"), AND([InputVariable("C"), InputVariable("B"), InputVariable("A")])])])
logic_simplifier = LogicSimplifier([RemoveRedundantANDs(), RemoveRedundantORs(), RemoveOperandRepeatedInside()])
print(logic_simplifier.simplify(logic_statement).get_string())
