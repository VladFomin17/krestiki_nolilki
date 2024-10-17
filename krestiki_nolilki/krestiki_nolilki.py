   # -*- coding: cp1251 -*-
   

def initialize_board():
    return [' ' for i in range(9)]  # Создает список из 9 пробелов

def print_board(board):
    print(" 1 | 2 | 3")
    print(" -----------")
    for i in range(3):
        new_func(board, i)
        print(" -----------")

def new_func(board, i):
    print(f"{i + 1} | {' | '.join(board[i * 3:i * 3 + 3])}")

def check_winner(board):
    # Все возможные комбинации выигрышных линий
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
        (0, 4, 8), (2, 4, 6)              # Диагонали
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]  # Возвращаем победителя ('X' или 'O')
    return None

def is_full(board):
    return ' ' not in board

def main():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        try:
            move = int(input(f"Игрок {current_player}, введите номер клетки (1-9): ")) - 1
            if board[move] != ' ':
                print("Эта клетка уже занята. Попробуйте снова.")
                continue
        except (ValueError, IndexError):
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue

        board[move] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Поздравляем! Игрок {winner} выиграл!")
            break
        
        if is_full(board):
            print_board(board)
            print("Игра закончилась вничью!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
