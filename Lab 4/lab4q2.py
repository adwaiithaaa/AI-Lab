from queue import PriorityQueue

ENTRY = (4, 1)
EXIT = (1, 8)

grid = [
 [1,1,1,1,1,1,1,1,1,1],
 [1,0,0,0,1,0,0,0,0,1],
 [1,0,1,0,1,0,1,1,0,1],
 [1,0,1,0,0,0,0,1,0,1],
 [1,0,0,0,1,1,0,0,0,1],
 [1,1,1,1,1,1,1,1,1,1]
]

heuristic = [
 [0,0,0,0,0,0,0,0,0,0],
 [0,8,7,6,0,4,3,2,1,0],
 [0,9,0,7,0,5,0,0,2,0],
 [0,10,0,8,7,6,5,0,3,0],
 [0,11,10,9,0,0,6,5,4,0],
 [0,0,0,0,0,0,0,0,0,0]
]

def make_node(state, parent, action, path_cost):
    return {
        "STATE": state,
        "PARENT": parent,
        "ACTION": action,
        "PATH_COST": path_cost
    }

def EXPAND(node):
    children = []
    x, y = node["STATE"]

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == 0:
            child = make_node(
                (nx, ny),
                node,
                (dx, dy),
                node["PATH_COST"] + 1
            )
            children.append(child)
    return children

def BEST_FIRST_SEARCH():
    node = make_node(ENTRY, None, None, 0)

    frontier = PriorityQueue()
    counter = 0  # Tie-breaker for nodes with same heuristic
    frontier.put((heuristic[ENTRY[0]][ENTRY[1]], counter, node))

    reached = {}
    reached[ENTRY] = node

    nodes_explored = 0

    while not frontier.empty():
        _, _, node = frontier.get()
        nodes_explored += 1

        if node["STATE"] == EXIT:
            return node, nodes_explored

        for child in EXPAND(node):
            s = child["STATE"]
            if s not in reached or child["PATH_COST"] < reached[s]["PATH_COST"]:
                reached[s] = child
                counter += 1
                frontier.put((heuristic[s[0]][s[1]], counter, child))

    return None, nodes_explored

goal_node, explored = BEST_FIRST_SEARCH()

path = []
n = goal_node
while n is not None:
    path.append(n["STATE"])
    n = n["PARENT"]

path.reverse()

print("Evacuation Path:", path)
print("Nodes Explored:", explored)
