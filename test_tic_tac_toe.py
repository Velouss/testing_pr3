import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_initial_board(self):
        game = TicTacToe()
        self.assertEqual(game.get_board(), [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_make_move(self):
        game = TicTacToe()
        game.make_move(0, 0, 'X')
        self.assertEqual(game.get_board(), [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_invalid_move(self):
        game = TicTacToe()
        result = game.make_move(0, 0, 'X')
        self.assertTrue(result)
        result = game.make_move(0, 0, 'O')
        self.assertFalse(result)

    def test_check_win(self):
        game = TicTacToe()
        game.make_move(0, 0, 'X')
        game.make_move(0, 1, 'X')
        game.make_move(0, 2, 'X')
        self.assertTrue(game.check_win('X'))

    def test_check_draw(self):
        game = TicTacToe()
        game.make_move(0, 0, 'X')
        game.make_move(0, 1, 'O')
        game.make_move(0, 2, 'X')
        game.make_move(1, 0, 'X')
        game.make_move(1, 1, 'O')
        game.make_move(1, 2, 'X')
        game.make_move(2, 0, 'O')
        game.make_move(2, 1, 'X')
        game.make_move(2, 2, 'O')
        self.assertTrue(game.check_draw())


if __name__ == '__main__':
    unittest.main()
