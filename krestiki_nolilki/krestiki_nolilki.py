   # -*- coding: cp1251 -*-
   

def initialize_board():
    return [' ' for i in range(9)]  # ������� ������ �� 9 ��������

def print_board(board):
    print(" 1 | 2 | 3")
    print(" -----------")
    for i in range(3):
        new_func(board, i)
        print(" -----------")

def new_func(board, i):
    print(f"{i + 1} | {' | '.join(board[i * 3:i * 3 + 3])}")

def check_winner(board):
    # ��� ��������� ���������� ���������� �����
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # �����������
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # ���������
        (0, 4, 8), (2, 4, 6)              # ���������
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]  # ���������� ���������� ('X' ��� 'O')
    return None

def is_full(board):
    return ' ' not in board

def main():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        try:
            move = int(input(f"����� {current_player}, ������� ����� ������ (1-9): ")) - 1
            if board[move] != ' ':
                print("��� ������ ��� ������. ���������� �����.")
                continue
        except (ValueError, IndexError):
            print("������������ ����. ������� ����� �� 1 �� 9.")
            continue

        board[move] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"�����������! ����� {winner} �������!")
            break
        
        if is_full(board):
            print_board(board)
            print("���� ����������� ������!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
