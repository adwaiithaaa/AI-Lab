graph = {
    "Syracuse": {"Buffalo": 150,"New York": 254,"Boston": 312,"Pittsburgh": 253},
    "Buffalo": {"Syracuse": 150,"Detroit": 256,"Cleveland": 189,"Pittsburgh": 215},
    "Detroit": {"Buffalo": 256,"Chicago": 283,"Cleveland": 169},
    "Chicago": {"Detroit": 283,"Cleveland": 345,"Indianapolis": 182},
    "Cleveland": {"Chicago": 345,"Detroit": 169,"Buffalo": 189,"Columbus": 144,"Pittsburgh": 134},
    "Columbus": {"Cleveland": 144,"Indianapolis": 176,"Pittsburgh": 185},
    "Indianapolis": {"Chicago": 182,"Columbus": 176},
    "Pittsburgh": {"Buffalo": 215,"Cleveland": 134,"Columbus": 185,"Philadelphia": 305,"Baltimore": 247,"Syracuse": 253},
    "Philadelphia": {"Pittsburgh": 305,"New York": 97,"Baltimore": 101},
    "Baltimore": {"Philadelphia": 101,"Pittsburgh": 247},
    "New York": {"Syracuse": 254,"Philadelphia": 97,"Boston": 215,"Providence": 181},
    "Boston": {"Syracuse": 312,"New York": 215,"Providence": 50,"Portland": 107},
    "Providence": {"Boston": 50,"New York": 181},
    "Portland": {"Boston": 107}
}

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    return cost

def bfs_all_paths(start, goal):
    queue = [[start]]
    all_paths = []

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current == goal:
            all_paths.append(path)
            continue

        for neighbor in graph[current]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append(new_path)

    return all_paths

def dfs_all_paths(start, goal, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    path.append(start)

    if start == goal:
        all_paths.append(path.copy())
    else:
        for neighbor in graph[start]:
            if neighbor not in path:
                dfs_all_paths(neighbor, goal, path, all_paths)

    path.pop()
    return all_paths

start_city = "Syracuse"
end_city = "Chicago"

print("BFS Paths from Syracuse to Chicago:\n")
bfs_paths = bfs_all_paths(start_city, end_city)

for p in bfs_paths:
    print(p, "Cost:", calculate_cost(p))


print("\n--------------------------------\n")

print("DFS Paths from Syracuse to Chicago:\n")
dfs_paths = dfs_all_paths(start_city, end_city)

for p in dfs_paths:
    print(p, "Cost:", calculate_cost(p))