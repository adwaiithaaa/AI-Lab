from queue import PriorityQueue

States = {0 : "Chicago", 1 : "Detroit", 2 : "Cleveland", 3 : "Columbus",4 : "Indianapolis", 
          5 : "Buffalo", 6 : "Pittsburgh", 7 : "Syracuse", 8 : "New York", 9 : "Philadelphia", 
          10 : "Baltimore", 11 : "Boston", 12 : "Providence", 13 : "Portland"}
INITIAL = 7      # 0 is Chicago
GOAL = 0        # 11 is Boston

# Rule Table (implemented as an adjacency matrix)

graph = [
 [0,1,1,0,1,0,0,0,0,0,0,0,0,0],  # 0 -> Chicago
 [1,0,0,0,0,1,0,0,0,0,0,0,0,0],  # 1 -> Detroit
 [1,0,0,1,0,1,1,0,0,0,0,0,0,0],  # 2 -> Cleveland
 [0,0,1,0,1,0,1,0,0,0,0,0,0,0],  # 3 -> Columbus
 [1,0,0,1,0,0,0,0,0,0,0,0,0,0],  # 4 -> Indianapolis
 [0,1,1,0,0,0,0,1,0,0,0,0,0,0],  # 5 -> Buffalo
 [0,0,1,1,0,0,0,0,0,1,0,0,0,0],  # 6 -> Pittsburgh
 [0,0,0,0,0,1,0,0,1,0,0,0,0,0],  # 7 -> Syracuse
 [0,0,0,0,0,0,0,1,0,1,0,1,1,0],  # 8 -> New York
 [0,0,0,0,0,0,1,0,1,0,1,0,0,0],  # 9 -> Philadelphia
 [0,0,0,0,0,0,0,0,0,1,0,0,0,0],  # 10 -> Baltimore
 [0,0,0,0,0,0,0,0,1,0,0,0,0,1],  # 11 -> Boston
 [0,0,0,0,0,0,0,0,1,0,0,0,0,0],  # 12 -> Providence
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0]   # 13 -> Portland
]

# Heuristic table (h(n)) -> it gives the distance from the specific city to end state

heuristic = [
0, 283, 345, 345, 182,
450, 460, 590, 790, 760,
720, 983, 920, 1070
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
    s = node["STATE"]
    for action in range(len(graph)):
        if graph[s][action] == 1:
            s_prime = action
            cost = node["PATH_COST"] + 1
            child = make_node(s_prime, node, action, cost)
            children.append(child)
    return children

def BEST_FIRST_SEARCH():
    node = make_node(INITIAL, None, None, 0)

    frontier = PriorityQueue()
    counter = 0  # Tie-breaker for nodes with same heuristic
    frontier.put((heuristic[node["STATE"]], counter, node))

    reached = {}
    reached[INITIAL] = node

    nodes_explored = 0

    while not frontier.empty():
        _, _, node = frontier.get()
        nodes_explored += 1

        if node["STATE"] == GOAL:
            return node, nodes_explored

        for child in EXPAND(node):
            s = child["STATE"]
            if s not in reached or child["PATH_COST"] < reached[s]["PATH_COST"]:
                reached[s] = child
                counter += 1
                frontier.put((heuristic[s], counter, child))

    return None, nodes_explored

goal_node, explored = BEST_FIRST_SEARCH()

path = []
n = goal_node
while n is not None:
    path.append(n["STATE"])
    n = n["PARENT"]

path.reverse()

print("Path from Chicago to Boston :")
for i in path :
    if i == 11 :
        print(States[i],end="\n")
    else : 
        print(States[i],end=" -> ")
print("Nodes explored:", explored)
