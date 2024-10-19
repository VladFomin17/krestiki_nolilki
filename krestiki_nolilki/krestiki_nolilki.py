def initialize_board():
    return [' ' for i in range(9)]  

def print_board(board):
    print("    1 | 2 | 3")
    print(" -----------")
    for i in range(3):
        print(f"{i + 1} | {' | '.join(board[i * 3:i * 3 + 3])}")
        print(" -----------")

def check_winner(board):
    
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != ' ':
            return board[a] 
    return None

def is_full(board):
    return ' ' not in board

def restart_game():
    print("Чтобы сыграть ещё раз, введите пробел")
    if input() == " ":
        main()