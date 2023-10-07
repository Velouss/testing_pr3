class TicTacToe:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def get_board(self):
        return self.board

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.switch_player()
            return True
        else:
            return False

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_win(self, player):
        # Проверяем выигрыш по строкам, столбцам и диагоналям
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))


def main():
    game = TicTacToe()
    while True:
        print_board(game.get_board())
        row = int(input(f"Player {game.current_player}, enter row (0-2): "))
        col = int(input(f"Player {game.current_player}, enter column (0-2): "))
        if game.make_move(row, col, game.current_player):
            if game.check_win(game.current_player):
                print_board(game.get_board())
                print(f"Player {game.current_player} wins!")
                break
            elif game.check_draw():
                print_board(game.get_board())
                print("It's a draw!")
                break

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

if __name__ == '__main__':
    main()
