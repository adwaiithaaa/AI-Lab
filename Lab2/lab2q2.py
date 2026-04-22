import queue

start = (7, 2, 4,5, 0, 6,8, 3, 1)

goal = (0, 1, 2,3, 4, 5,6, 7, 8)

stack = queue.LifoQueue()
stack.put(start)

visited = set()
visited.add(start)

count = 0

while not stack.empty():
    current = stack.get()
    count += 1

    if current == goal:
        break

    zero = current.index(0)
    row = zero // 3
    col = zero % 3

    moves = []

    if row > 0:
        moves.append(zero - 3)
    if row < 2:
        moves.append(zero + 3)
    if col > 0:
        moves.append(zero - 1)
    if col < 2:
        moves.append(zero + 1)

    for move in moves:
        new_state = list(current)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        new_state = tuple(new_state)

        if new_state not in visited:
            visited.add(new_state)
            stack.put(new_state)

print("Number of states explored:", count)