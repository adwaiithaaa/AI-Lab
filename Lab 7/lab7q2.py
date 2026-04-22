import random
import math

N = 8
TRIALS = 50

# Generate Board
def generate_board():
    board = [[0]*N for _ in range(N)]
    for col in range(N):
        row = random.randint(0, N-1)
        board[row][col] = 1
    return board

# Heuristic Function
def heuristic(board):
    conflicts = 0
    queens = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queens.append((i, j))

    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            r1, c1 = queens[i]
            r2, c2 = queens[j]

            if r1 == r2 or abs(r1-r2) == abs(c1-c2):
                conflicts += 1

    return conflicts

# Generate Neighbours
def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if board[row][col] == 1:
                current_row = row
                break

        for new_row in range(N):
            if new_row != current_row:
                new_board = [r[:] for r in board]
                new_board[current_row][col] = 0
                new_board[new_row][col] = 1
                neighbors.append(new_board)

    return neighbors

# First Choice Hill Climbing
def first_choice(board):
    steps = 0
    current = board
    current_h = heuristic(current)

    while True:
        neighbors = get_neighbors(current)
        random.shuffle(neighbors)

        improved = False
        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < current_h:
                current = neighbor
                current_h = h
                steps += 1
                improved = True
                break

        if not improved:
            status = "SOLVED" if current_h == 0 else "FAIL"
            return current_h, steps, status

# Random Restart Hill Climbing
def random_restart(max_restarts=10):
    total_steps = 0

    for _ in range(max_restarts):
        board = generate_board()
        h, steps, status = first_choice(board)
        total_steps += steps

        if status == "SOLVED":
            return h, total_steps, "SOLVED"

    return h, total_steps, "FAIL"

# Simulated Annealing
def simulated_annealing(board):
    current = board
    current_h = heuristic(current)
    steps = 0

    T = 100
    cooling_rate = 0.95

    while T > 0.1:
        if current_h == 0:
            return current_h, steps, "SOLVED"

        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)
        next_h = heuristic(next_state)

        delta = next_h - current_h

        if delta < 0:
            current = next_state
            current_h = next_h
        else:
            probability = math.exp(-delta / T)
            if random.random() < probability:
                current = next_state
                current_h = next_h

        T *= cooling_rate
        steps += 1

    status = "SOLVED" if current_h == 0 else "FAIL"
    return current_h, steps, status

# Run Experiments
def run_experiment(algorithm_name):
    success = 0
    total_steps = 0

    for _ in range(TRIALS):

        if algorithm_name == "First Choice":
            board = generate_board()
            h, steps, status = first_choice(board)

        elif algorithm_name == "Random Restart":
            h, steps, status = random_restart()

        elif algorithm_name == "Simulated Annealing":
            board = generate_board()
            h, steps, status = simulated_annealing(board)

        if status == "SOLVED":
            success += 1

        total_steps += steps

    return success, total_steps

# Compare Results
algorithms = ["First Choice", "Random Restart", "Simulated Annealing"]

print("\nComparison Over 50 Trials\n")
print("Algorithm                | Success | Avg Steps")
print("------------------------------------------------")

for algo in algorithms:
    success, total_steps = run_experiment(algo)
    avg_steps = total_steps / TRIALS
    print(f"{algo:25} | {success:7} | {avg_steps:.2f}")