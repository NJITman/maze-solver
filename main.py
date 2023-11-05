from graphics import Window, Point, Line, Cell
from maze import Maze

def main():
  win = Window(800, 600, "Maze Solver")
  # point1 = Point(0, 0)
  # point2 = Point(100, 100)
  # line = Line(point1, point2)
  # win.draw_line(line, "black")
  # point1_1 = Point(10, 10)
  # point1_2 = Point(20, 20)
  # cell1 = Cell(point1_1, point1_2, True, True, True, True)
  # cell1.draw(win.canvas, "black")
  # point2_1 = Point(30, 30)
  # point2_2 = Point(40, 40)
  # cell2 = Cell(point2_1, point2_2, True, True, True, True)
  # cell2.draw(win.canvas, "black")
  # cell1.draw_move(win.canvas, cell2, True)
  maze = Maze(10, 10, 10, 10, 10, 10, seed=0, window=win)
  # maze = Maze(100, 100, 5, 5, 50, 50, seed=0, window=win)
  maze.solve()
  win.wait_for_close()


if __name__ == "__main__":
  main()