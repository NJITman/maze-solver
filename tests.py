import unittest
from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
          len(m1.get_cells()),
          num_cols,
        )
        self.assertEqual(
          len(m1.get_cells()[0]),
          num_rows,
        )
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
          m1.get_cells()[0][0].get_top_wall(),
          False,
        )
        self.assertEqual(
          m1.get_cells()[num_cols - 1][num_rows - 1].get_bottom_wall(),
          False,
        )
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in range(num_cols):
          for row in range(num_rows):
            self.assertEqual(
              m1.get_cells()[col][row].get_visited(),
              False,
            )


if __name__ == "__main__":
    unittest.main()