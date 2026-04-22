import random

N = 8


# Generate random board
def random_board():
    return [random.randint(0, N - 1) for _ in range(N)]


# Heuristic: count attacking pairs
def heuristic(board):
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:  # Same row
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):  # Same diagonal
                attacks += 1
    return attacks


# Print board nicely
def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Generate neighbors
def get_neighbors(board):
    neighbors = []
    for col in range(N):
        for row in range(N):
            if row != board[col]:
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors


# Steepest Ascent Hill Climbing (with printing)
def steepest_hill_climb(board):
    step = 0

    print("Initial Board (Step 0)")
    print("Board:", board)
    print("Heuristic:", heuristic(board))
    print_board(board)

    while True:
        current_h = heuristic(board)
        neighbors = get_neighbors(board)

        best = board
        best_h = current_h

        for n in neighbors:
            h = heuristic(n)
            if h < best_h:
                best = n
                best_h = h

        if best_h >= current_h:
            print("No better neighbor found.")
            return board, best_h, step

        board = best
        step += 1

        print("Step", step)
        print("Board:", board)
        print("Heuristic:", best_h)
        print_board(board)


# -------------------------
# MAIN PROGRAM (50 RUNS)
# -------------------------

success_count = 0

for run in range(1, 51):

    print("=================================================")
    print("Run Number:", run)
    print("=================================================")

    board = random_board()
    initial_h = heuristic(board)

    final_board, final_h, steps = steepest_hill_climb(board)

    print("Final Result for Run", run)
    print("Initial Heuristic:", initial_h)
    print("Final Heuristic:", final_h)
    print("Total Steps:", steps)

    if final_h == 0:
        print("Status: Solved")
        success_count += 1
    else:
        print("Status: Failed (Local Minimum)")

    print("\n\n")


# Final Summary
print("=================================================")
print("FINAL SUMMARY AFTER 50 RUNS")
print("=================================================")
print("Total Solved:", success_count)
print("Total Failed:", 50 - success_count)
print("Success Rate:", (success_count / 50) * 100, "%")