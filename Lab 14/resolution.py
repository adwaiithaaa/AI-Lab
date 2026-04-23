

def backward_chaining(rules, facts, goal):
    if goal in facts:
        print(f"{goal} found in facts")
        return True

    for condition, result in rules:
        if result == goal:
            print(f"Checking Rule: {condition} -> {result}")
            if all(backward_chaining(rules, facts, c) for c in condition):
                return True

    return False


print("===== Backward Chaining : (a) =====")

rules_a = [
    (["P"], "Q"),
    (["R"], "Q"),
    (["A"], "P"),
    (["B"], "R")
]

facts_a = ["A", "B"]
goal_a = "Q"

if backward_chaining(rules_a, facts_a, goal_a):
    print(f"Conclusion: {goal_a} is TRUE")
else:
    print(f"Conclusion: {goal_a} is FALSE")


print("\n===== Backward Chaining : (b) =====")

rules_b = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["E"], "C")
]

facts_b = ["A", "E"]
goal_b = "D"

if backward_chaining(rules_b, facts_b, goal_b):
    print(f"Conclusion: {goal_b} is TRUE")
else:
    print(f"Conclusion: {goal_b} is FALSE")