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


if __name__ == '__main__':
    unittest.main()
