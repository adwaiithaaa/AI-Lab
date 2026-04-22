graph = {
    "Chicago": [("Detroit", 283), ("Indianapolis", 182), ("Cleveland", 345)],
    "Detroit": [("Chicago", 283), ("Buffalo", 256), ("Cleveland", 169)],
    "Buffalo": [("Detroit", 256), ("Syracuse", 150), ("Cleveland", 189)],
    "Syracuse": [("Buffalo", 150), ("New York", 254), ("Boston", 312)],
    "Boston": [("Syracuse", 312), ("Providence", 50), ("New York", 215)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "New York": [("Syracuse", 254), ("Boston", 215), ("Philadelphia", 97), ("Providence", 181)],
    "Philadelphia": [("New York", 97), ("Baltimore", 101), ("Pittsburgh", 305)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Pittsburgh": [("Cleveland", 134), ("Buffalo", 215), ("Philadelphia", 305), ("Baltimore", 247)],
    "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Buffalo", 189), ("Pittsburgh", 134), ("Columbus", 144)],
    "Columbus": [("Cleveland", 144), ("Indianapolis", 176), ("Pittsburgh", 185)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)]
}


import math

def minimax(city, depth, maximizing, visited, counter):
    counter[0] += 1

    if depth == 0:
        return 0

    if maximizing:
        max_eval = -math.inf
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                eval = cost + minimax(neighbor, depth-1, False, visited, counter)
                visited.remove(neighbor)
                max_eval = max(max_eval, eval)
        return max_eval if max_eval != -math.inf else 0

    else:
        min_eval = math.inf
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                eval = cost + minimax(neighbor, depth-1, True, visited, counter)
                visited.remove(neighbor)
                min_eval = min(min_eval, eval)
        return min_eval if min_eval != math.inf else 0
    


def alpha_beta(city, depth, alpha, beta, maximizing, visited, counter):
    counter[0] += 1

    if depth == 0:
        return 0

    if maximizing:
        max_eval = -math.inf
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                eval = cost + alpha_beta(neighbor, depth-1, alpha, beta, False, visited, counter)
                visited.remove(neighbor)

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break   # PRUNING

        return max_eval if max_eval != -math.inf else 0

    else:
        min_eval = math.inf
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                eval = cost + alpha_beta(neighbor, depth-1, alpha, beta, True, visited, counter)
                visited.remove(neighbor)

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                if beta <= alpha:
                    break   # PRUNING

        return min_eval if min_eval != math.inf else 0
    

start_city = "Buffalo"
depth = 20

# Minimax
counter_minimax = [0]
visited = set([start_city])
res_minimax = minimax(start_city, depth, True, visited, counter_minimax)

# Alpha-Beta
counter_ab = [0]
visited = set([start_city])
res_ab = alpha_beta(start_city, depth, -math.inf, math.inf, True, visited, counter_ab)

print("Minimax Result:", res_minimax)
print("Alpha-Beta Result:", res_ab)

print("\nNodes explored (Minimax):", counter_minimax[0])
print("Nodes explored (Alpha-Beta):", counter_ab[0])

gain = ((counter_minimax[0] - counter_ab[0]) / counter_minimax[0]) * 100
print("Efficiency Gain: {:.2f}%".format(gain))