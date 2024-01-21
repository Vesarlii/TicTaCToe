import random

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('-' * 9)

def check_winner(board, player):
    for i in range(0, 3):
        # Sprawdza wiersze
        if all(board[i * 3 + j] == player for j in range(3)):
            return True
        # Sprawdza kolumny
        if all(board[i + j * 3] == player for j in range(3)):
            return True

    # Sprawdza przekątne
    if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def player_move(board):
    while True:
        try:
            move = int(input('Twój ruch (1-9): '))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                return move - 1
            else:
                print('Nieprawidłowy ruch. Spróbuj ponownie.')
        except ValueError:
            print('Wprowadź liczbę.')

def computer_move(board):
    available_moves = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(available_moves)

def main():
    while True:
        board = [' '] * 9
        player_symbol = 'X'
        computer_symbol = 'O'

        while True:
            print_board(board)

            # Gracz wykonuje ruch
            player_position = player_move(board)
            board[player_position] = player_symbol

            # Sprawdza, czy gracz wygrał
            if check_winner(board, player_symbol):
                print_board(board)
                print('Gratulacje! Wygrałeś!')
                break

            # Sprawdza, czy plansza jest pełna (remis)
            if is_board_full(board):
                print_board(board)
                print('Remis!')
                break

            # Komputer wykonuje ruch
            computer_position = computer_move(board)
            board[computer_position] = computer_symbol

            # Sprawdza, czy komputer wygrał
            if check_winner(board, computer_symbol):
                print_board(board)
                print('Przegrałeś. Spróbuj ponownie.')
                break

        play_again = input('Czy chcesz zagrać ponownie? (tak/nie): ')
        if play_again.lower() != 'tak':
            break

if __name__ == "__main__":
    main()