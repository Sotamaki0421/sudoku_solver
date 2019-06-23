import unittest
from dfs import dfs
from board import Board
from sudoku import Sudoku

# Problem source: https://www.websudoku.com/

class TestSudoku(unittest.TestCase):
  def test_easy_1(self):
    board = Board([[6, 0, 0, 9, 2, 0, 0, 3, 8],
                   [3, 0, 0, 6, 7, 0, 0, 1, 5],
                   [0, 1, 9, 0, 3, 0, 0, 0, 0],
                   [0, 0, 0, 3, 6, 0, 0, 5, 0],
                   [2, 6, 0, 0, 0, 0, 0, 7, 3],
                   [0, 4, 0, 0, 5, 7, 0, 0, 0],
                   [0, 0, 0, 0, 8, 0, 5, 2, 0],
                   [4, 8, 0, 0, 9, 3, 0, 0, 7],
                   [5, 7, 0, 0, 1, 2, 0, 0, 9]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_easy_2(self):
    board = Board([[2, 7, 4, 0, 0, 0, 5, 8, 0],
                   [0, 0, 0, 0, 0, 8, 2, 0, 0],
                   [6, 0, 3, 5, 4, 2, 0, 0, 0],
                   [3, 0, 1, 2, 0, 0, 8, 0, 0],
                   [0, 0, 0, 8, 6, 4, 0, 0, 0],
                   [0, 0, 8, 0, 0, 3, 6, 0, 5],
                   [0, 0, 0, 3, 2, 7, 9, 0, 8],
                   [0, 0, 2, 1, 0, 0, 0, 0, 0],
                   [0, 1, 9, 0, 0, 0, 3, 2, 7]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_easy_3(self):
    board = Board([[0, 0, 0, 0, 9, 2, 0, 0, 0],
                   [0, 7, 9, 6, 0, 5, 0, 8, 0],
                   [3, 0, 0, 1, 0, 0, 0, 0, 5],
                   [0, 3, 0, 0, 0, 6, 0, 4, 2],
                   [0, 2, 6, 5, 8, 4, 3, 1, 0],
                   [5, 4, 0, 2, 0, 0, 0, 6, 0],
                   [1, 0, 0, 0, 0, 3, 0, 0, 6],
                   [0, 5, 0, 7, 0, 1, 8, 3, 0],
                   [0, 0, 0, 4, 2, 0, 0, 0, 0]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_medium(self):
    board = Board([[0, 0, 0, 0, 8, 0, 0, 0, 0],
                   [4, 5, 8, 0, 0, 0, 0, 2, 0],
                   [6, 9, 2, 0, 4, 0, 0, 0, 1],
                   [0, 0, 0, 7, 0, 0, 3, 8, 2],
                   [0, 1, 0, 0, 0, 0, 0, 6, 0],
                   [2, 7, 5, 0, 0, 3, 0, 0, 0],
                   [7, 0, 0, 0, 2, 0, 9, 1, 3],
                   [0, 2, 0, 0, 0, 0, 6, 5, 8],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_hard(self):
    board = Board([[7, 0, 6, 5, 0, 9, 0, 4, 0],
                   [0, 0, 0, 3, 7, 0, 0, 9, 0],
                   [9, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 9, 0, 0, 0, 0, 0, 0, 4],
                   [1, 0, 7, 0, 4, 0, 5, 0, 3],
                   [2, 0, 0, 0, 0, 0, 0, 7, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 6],
                   [0, 1, 0, 0, 3, 4, 0, 0, 0],
                   [0, 6, 0, 8, 0, 7, 1, 0, 9]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_evil(self):
    board = Board([[0, 1, 8, 0, 6, 0, 0, 0, 0],
                   [3, 0, 0, 0, 0, 9, 0, 0, 0],
                   [0, 0, 9, 0, 0, 3, 4, 0, 0],
                   [0, 9, 0, 1, 0, 0, 0, 0, 5],
                   [0, 4, 2, 0, 0, 0, 7, 1, 0],
                   [5, 0, 0, 0, 0, 2, 0, 8, 0],
                   [0, 0, 4, 5, 0, 0, 6, 0, 0],
                   [0, 0, 0, 8, 0, 0, 0, 0, 7],
                   [0, 0, 0, 0, 7, 0, 8, 4, 0]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())

  def test_extra(self):
    board = Board([[1, 4, 0, 0, 0, 0, 9, 0, 0],
                   [0, 0, 3, 8, 6, 1, 0, 0, 0],
                   [5, 0, 0, 0, 0, 0, 0, 0, 0],
                   [2, 0, 9, 0, 0, 0, 0, 7, 0],
                   [0, 0, 0, 5, 2, 0, 0, 0, 0],
                   [0, 0, 1, 6, 0, 0, 3, 5, 0],
                   [0, 8, 0, 0, 0, 0, 7, 0, 6],
                   [0, 0, 0, 3, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    self.assertTrue(boards[-1].filled())
    self.assertTrue(boards[-1].verify())


if __name__ == '__main__':
  unittest.main(verbosity=2)