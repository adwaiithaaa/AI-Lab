TOTAL_G = 3
TOTAL_B = 3

MOVES = [
    (1,0),(2,0),
    (0,1),(0,2),
    (1,1)
]

def valid_state(g_left, b_left):
    g_right = TOTAL_G - g_left
    b_right = TOTAL_B - b_left

    if g_left < 0 or b_left < 0 or g_left > TOTAL_G or b_left > TOTAL_B:
        return False

    if g_left > 0 and b_left > g_left:
        return False

    if g_right > 0 and b_right > g_right:
        return False

    return True

def successors(state):
    g_left, b_left, boat = state
    next_states = []

    for g, b in MOVES:
        if boat == 0:
            new = (g_left - g, b_left - b, 1)
        else:
            new = (g_left + g, b_left + b, 0)

        if valid_state(new[0], new[1]):
            next_states.append(new)

    return next_states

def dls(state, goal, limit, path, visited, explored_count, explored_states):
    explored_count[0] += 1
    explored_states.append(state)

    if state == goal:
        return path

    if limit == 0:
        return "cutoff"

    cutoff_occured = False

    for child in successors(state):
        if child not in visited:
            visited.add(child)
            result = dls(child, goal, limit-1,
                         path+[child], visited, explored_count, explored_states)

            if result == "cutoff":
                cutoff_occured = True
            elif result != None:
                return result

            visited.remove(child)

    return "cutoff" if cutoff_occured else None

def run_dls(limit):
    start = (3,3,0)
    goal = (0,0,1)
    explored_count = [0]
    explored_states = []

    result = dls(start, goal, limit,
                 [start], set([start]), explored_count, explored_states)

    return result, explored_count[0], explored_states

result, explored_count, explored_states = run_dls(3)
print("Result:", result)
print("Explored Count:", explored_count)
print("Explored States:", explored_states)