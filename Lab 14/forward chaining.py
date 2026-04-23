

def forward_chaining(rules, facts, goal):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for condition, result in rules:
            if set(condition).issubset(inferred) and result not in inferred:
                print(f"Applying Rule: {condition} -> {result}")
                inferred.add(result)
                changed = True

    print("Final Facts:", inferred)

    if goal in inferred:
        print(f"Conclusion: {goal} is TRUE")
    else:
        print(f"Conclusion: {goal} is FALSE")


print("===== Forward Chaining : (a) =====")

rules_a = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]

facts_a = ["A", "B", "M"]
goal_a = "Q"

forward_chaining(rules_a, facts_a, goal_a)


print("\n===== Forward Chaining : (b) =====")

rules_b = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]

facts_b = ["A", "E"]
goal_b = "F"

forward_chaining(rules_b, facts_b, goal_b)