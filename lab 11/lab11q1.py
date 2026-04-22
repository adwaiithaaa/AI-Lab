

# Define colors
colors = ["Red", "Green", "Blue", "Yellow"]

graph = {
    "Ahmedabad": ["Gandhinagar", "Kheda", "Anand"],
    "Gandhinagar": ["Ahmedabad", "Sabarkantha"],
    "Kheda": ["Ahmedabad", "Anand"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara"],
    "Vadodara": ["Anand", "Panchmahal"],
    "Panchmahal": ["Vadodara", "Dahod"],
    "Dahod": ["Panchmahal"]
}

# Store result
result = {}


def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def solve():
    for node in graph:
        for color in colors:
            if is_safe(node, color):
                result[node] = color
                break


solve()

# Output
for district in result:
    print(district, "->", result[district])

    print("Color Assignment:")

print("\nTotal colors used:", len(set(result.values())))