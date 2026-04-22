graph = {
    "Raj": ["Priya", "Sunil"],

    "Priya": ["Raj", "Aarav", "Neha1"],
    "Aarav": ["Priya", "Neha2", "Arjun1"],

    "Sunil": ["Raj", "Akash", "Sneha1"],
    "Akash": ["Sunil", "Neha1"],

    "Neha1": ["Priya", "Akash", "Sneha2"],
    "Neha2": ["Aarav"],  

    "Sneha1": ["Sunil", "Rahul"],
    "Sneha2": ["Neha1", "Rahul"],

    "Rahul": ["Sneha1", "Sneha2", "Maya", "Pooja1"],

    "Maya": ["Rahul", "Arjun2"],
    "Arjun2": ["Maya"],

    "Pooja1": ["Rahul", "Arjun1"],
    "Pooja2": ["Arjun1"],
    "Arjun1": ["Aarav", "Pooja1", "Pooja2"]
}


def bfs_tree(start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        current = queue.pop(0)
        visited.append(current)

        for friend in graph[current]:
            if friend not in visited and friend not in queue:
                parent[friend] = current
                queue.append(friend)

    return parent

def dfs_tree(start, visited=None, parent=None):
    if visited is None:
        visited = []
    if parent is None:
        parent = {start: None}

    visited.append(start)

    for friend in graph[start]:
        if friend not in visited:
            parent[friend] = start
            dfs_tree(friend, visited, parent)

    return parent

start_node = "Raj"

print("BFS TREE (Parent -> Child):\n")
bfs_parent = bfs_tree(start_node)
for node in bfs_parent:
    if bfs_parent[node] is not None:
        print(bfs_parent[node], "->", node)

print("\n-----------------------------\n")

print("DFS TREE (Parent -> Child):\n")
dfs_parent = dfs_tree(start_node)
for node in dfs_parent:
    if dfs_parent[node] is not None:
        print(dfs_parent[node], "->", node)