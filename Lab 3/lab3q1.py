
environment = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Dirty"
}

location = "A"

cost = 0

rules = {
    ("A", "Dirty"): "Suck",
    ("B", "Dirty"): "Suck",
    ("C", "Dirty"): "Suck",

    ("A", "Clean"): "Move_Right",
    ("B", "Clean"): "Move_Right",
    ("C", "Clean"): "NoOp"
}

print("Percept\t\tAction\t\tLocation")

for step in range(10):

    
    percept = (location, environment[location])

    action = rules[percept]

    print(percept, "\t", action, "\t", location)

    if action == "Suck":
        environment[location] = "Clean"
        cost += 1

    elif action == "Move_Right":
        if location == "A":
            location = "B"
        elif location == "B":
            location = "C"
        cost += 1

    elif action == "NoOp":
        break

print("\nFinal Environment:", environment)
print("Total Performance Cost:", cost)
