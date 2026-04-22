from itertools import product

class Symbol:
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        return model[self.name]

def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMPLIES(p, q):
    return (not p) or q

def BICONDITIONAL(p, q):
    return p == q


def truth_table(variables, expression_func):
    print("\nTruth Table:")
    print(" | ".join(variables) + " | Result")
    print("-" * 30)

    for values in product([False, True], repeat=len(variables)):
        model = dict(zip(variables, values))
        result = expression_func(model)

        row = " | ".join(['T' if model[v] else 'F' for v in variables])
        print(row + " | " + ('T' if result else 'F'))



# 1. ~P -> Q
def expr1(m):
    return IMPLIES(NOT(m['P']), m['Q'])

# 2. ~P ∧ ~Q
def expr2(m):
    return AND(NOT(m['P']), NOT(m['Q']))

# 3. ~P ∨ ~Q
def expr3(m):
    return OR(NOT(m['P']), NOT(m['Q']))

# 4. ~P -> Q (same as 1)
def expr4(m):
    return IMPLIES(NOT(m['P']), m['Q'])

# 5. ~P <-> Q
def expr5(m):
    return BICONDITIONAL(NOT(m['P']), m['Q'])

# 6. (P ∨ Q) ∧ (~P -> Q)
def expr6(m):
    return AND(OR(m['P'], m['Q']), IMPLIES(NOT(m['P']), m['Q']))

# 7. (P ∨ Q) -> R
def expr7(m):
    return IMPLIES(OR(m['P'], m['Q']), m['R'])

# 8. ((P ∨ Q) -> R) <-> ((~P ∧ ~Q) -> ~R)
def expr8(m):
    left = IMPLIES(OR(m['P'], m['Q']), m['R'])
    right = IMPLIES(AND(NOT(m['P']), NOT(m['Q'])), NOT(m['R']))
    return BICONDITIONAL(left, right)

# 9. ((P -> Q) ∧ (Q -> R)) -> (P -> R)
def expr9(m):
    left = AND(IMPLIES(m['P'], m['Q']), IMPLIES(m['Q'], m['R']))
    right = IMPLIES(m['P'], m['R'])
    return IMPLIES(left, right)

# 10. ((P -> (Q ∨ R)) -> (~P ∧ ~Q ∧ ~R))
def expr10(m):
    left = IMPLIES(m['P'], OR(m['Q'], m['R']))
    right = AND(AND(NOT(m['P']), NOT(m['Q'])), NOT(m['R']))
    return IMPLIES(left, right)



print("Expression 1")
truth_table(['P', 'Q'], expr1)

print("\nExpression 2")
truth_table(['P', 'Q'], expr2)

print("\nExpression 3")
truth_table(['P', 'Q'], expr3)

print("\nExpression 4")
truth_table(['P', 'Q'], expr4)

print("\nExpression 5")
truth_table(['P', 'Q'], expr5)

print("\nExpression 6")
truth_table(['P', 'Q'], expr6)

print("\nExpression 7")
truth_table(['P', 'Q', 'R'], expr7)

print("\nExpression 8")
truth_table(['P', 'Q', 'R'], expr8)

print("\nExpression 9")
truth_table(['P', 'Q', 'R'], expr9)

print("\nExpression 10")
truth_table(['P', 'Q', 'R'], expr10)