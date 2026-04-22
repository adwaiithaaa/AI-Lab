from collections import deque
import copy


variables = ["P1", "P2", "P3", "P4", "P5", "P6"]


domains = {v: ["R1", "R2", "R3"] for v in variables}


constraints = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}


def get_arcs():
    return deque((xi, xj) for xi in variables for xj in constraints[xi])


def revise(xi, xj, domains):
    revised = False
    for x in domains[xi][:]:
        if all(x == y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised


def ac3(domains, trace=False):
    queue = get_arcs()
    steps = []
    
    while queue:
        xi, xj = queue.popleft()
        changed = revise(xi, xj, domains)
        
        if trace and len(steps) < 5:
            if changed:
                steps.append(f"Arc ({xi},{xj}) -> domain reduced")
            else:
                steps.append(f"Arc ({xi},{xj}) -> no change")
        
        if changed:
            if not domains[xi]:
                return False, steps
            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    
    return True, steps



domains_copy = copy.deepcopy(domains)
result, steps = ac3(domains_copy, trace=True)

print("Arc Consistent:", result)

print("\nFirst 5 Arc Checks:")
for s in steps:
    print(s)

print("\nDomains after AC-3:")
for v in domains_copy:
    print(v, ":", domains_copy[v])

# Special case: P1 = R1
print("\n--- Case: P1 = R1 ---")
domains_case = copy.deepcopy(domains)
domains_case["P1"] = ["R1"]

result2, _ = ac3(domains_case)

print("Arc Consistent after assignment:", result2)
print("Updated Domains:")
for v in domains_case:
    print(v, ":", domains_case[v])

# Final conclusion
print("\nConclusion:")
print("The CSP is arc-consistent.")
print("No domain becomes empty.")
print("After assigning P1=R1, domains reduce but remain consistent.")