import math

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows Wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns Wins
        [0, 4, 8], [2, 4, 6]             # Diagonals Wins
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Draw'
    return None

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing, node_counter):
    node_counter[0] += 1
    winner = check_winner(board)
    
    # Static evaluation
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False, node_counter)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True, node_counter)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def find_best_move(board, is_maximizing):
    best_move = -1
    node_counter = [0]
    
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, 0, False, node_counter)
            board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, 0, True, node_counter)
            board[move] = ' '
            if score < best_score:
                best_score = score
                best_move = move
                
    return best_move, node_counter[0]

def visualize_tree(board, is_maximizing, depth=0, max_depth=2):
    """Recursively prints a text-based representation of the search tree."""
    if depth > max_depth:
        return
        
    indent = "    " * depth
    player = 'X' if is_maximizing else 'O'
    board_str = "|" + "|".join([x if x != ' ' else '_' for x in board]) + "|"
    
    winner = check_winner(board)
    if winner or depth == max_depth:
        score = 0
        if winner == 'X': score = 10
        elif winner == 'O': score = -10
        print(f"{indent}L- {board_str} (Depth {depth}, Node Score: {score})")
        return

    print(f"{indent}+- {board_str} (Depth {depth}, {player}'s turn to play)")
    
    for move in get_available_moves(board):
        board[move] = player
        visualize_tree(board, not is_maximizing, depth + 1, max_depth)
        board[move] = ' '

if __name__ == "__main__":
    initial_board = [' '] * 9
    
    print("==================================================")
    print("      MINIMAX TIC-TAC-TOE IMPLEMENTATION          ")
    print("==================================================")
    
    print("\n1. Visualizing a partial search tree from an empty board (Depth <= 2):")
    visualize_tree(initial_board.copy(), is_maximizing=True, max_depth=2)
    
    print("\n2. Evaluating Minimax Performance:")
    # We evaluate an almost empty board and some mid-game states
    states_to_test = [
        ("Empty Board", [' '] * 9, True),
        ("Mid Game 1", ['X', 'O', 'X', ' ', 'O', ' ', ' ', ' ', ' '], True),
        ("Late Game", ['X', 'O', 'X', 'O', 'O', 'X', ' ', ' ', ' '], True)
    ]
    
    for name, board_state, is_max in states_to_test:
        print(f"\nEvaluating state: {name}")
        print_board(board_state)
        best_move, nodes_evaluated = find_best_move(board_state, is_maximizing=is_max)
        print(f"-> Optimal move for 'X': index {best_move}")
        print(f"-> Total states (nodes) evaluated: {nodes_evaluated}")