from __future__ import annotations
from graphics import Window, Point, Cell
import random
from time import sleep

class Maze:
  def __init__(self, x1:int, y1:int, num_rows:int, num_cols:int, cell_size_x:int, cell_size_y:int, seed:bool=None, window:Window=None):
    self.window = window
    if seed is not None:
      random.seed(seed)
    self.__x1 = x1
    self.__y1 = y1
    self.__num_rows = num_rows
    self.__num_cols = num_cols
    self.__cell_size_x = cell_size_x
    self.__cell_size_y = cell_size_y
    self.__exit_corner = Point(x1 + (num_cols * cell_size_x), y1 + (num_rows * cell_size_y))  
    self.__cells = []
    self.__create_cells()

  def get_cells(self) -> [Cell]:
    return self.__cells

  def get_cell(self, row:int, col:int) -> Cell:
    return self.__cells[col][row]

  def __create_cells(self):
    self.__cells = []
    for col in range(self.__num_cols):
      column = []
      for row in range(self.__num_rows):
        x1 = self.__x1 + (col * self.__cell_size_x)
        y1 = self.__y1 + (row * self.__cell_size_y)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell = Cell(Point(x1, y1), Point(x2, y2), True, True, True, True)
        column.append(cell)
      self.__cells.append(column)
    for col in range(self.__num_cols):
      for row in range(self.__num_rows):
        self.__draw_cell(row, col)
    self.__break_entrance_and_exit()
    self.__break_walls_recursive(0, 0)
    self.__reset_cells_visited()

  def __draw_cell(self, row, col):
    if self.window is not None:
      cell = self.get_cell(row, col)
      cell.draw(self.window.canvas, "black")
      self.__animate(0.05)

  def __animate(self, time:float=0.0):
    self.window.redraw()
    if time > 0:
      sleep(time)

  def __break_entrance_and_exit(self):
    self.__cells[0][0].set_top_wall(False)
    self.__cells[self.__num_cols - 1][self.__num_rows - 1].set_bottom_wall(False)
    self.__draw_cell(0, 0)
    self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)

  def __get_unvisited_neighbors(self, row:int, col:int) -> [(int, int)]:
    neighbors = []
    if row > 0 and not self.get_cell(row - 1, col).get_visited():
      neighbors.append((row - 1, col))
    if row < self.__num_rows - 1 and not self.get_cell(row + 1, col).get_visited():
      neighbors.append((row + 1, col))
    if col > 0 and not self.get_cell(row, col - 1).get_visited():
      neighbors.append((row, col - 1))
    if col < self.__num_cols - 1 and not self.get_cell(row, col + 1).get_visited():
      neighbors.append((row, col + 1))
    return neighbors

  def __break_walls_recursive(self, row:int, col:int):
    cell = self.get_cell(row, col)
    cell.set_visited(True)
    self.__draw_cell(row, col)
    while True:
      neighbors = self.__get_unvisited_neighbors(row, col)
      if len(neighbors) == 0:
        break
      neighbor = neighbors[int(random.random() * len(neighbors))]
      if neighbor[0] == row - 1:
        self.get_cell(row, col).set_top_wall(False)
        self.get_cell(neighbor[0], neighbor[1]).set_bottom_wall(False)
      elif neighbor[0] == row + 1:
        self.get_cell(row, col).set_bottom_wall(False)
        self.get_cell(neighbor[0], neighbor[1]).set_top_wall(False)
      elif neighbor[1] == col - 1:
        self.get_cell(row, col).set_left_wall(False)
        self.get_cell(neighbor[0], neighbor[1]).set_right_wall(False)
      elif neighbor[1] == col + 1:
        self.get_cell(row, col).set_right_wall(False)
        self.get_cell(neighbor[0], neighbor[1]).set_left_wall(False)
      self.__draw_cell(row, col)
      self.__draw_cell(neighbor[0], neighbor[1])
      self.__break_walls_recursive(neighbor[0], neighbor[1])

  def __reset_cells_visited(self):
    for col in range(self.__num_cols):
      for row in range(self.__num_rows):
        self.get_cell(row, col).set_visited(False)

  def solve(self) -> bool:
    self.__reset_cells_visited()
    self.__solve_recursive(0, 0)

  def __solve_recursive(self, row:int, col:int) -> bool:
    cell = self.get_cell(row, col)
    self.__draw_cell(row, col)
    self.__animate(0.05)
    cell.set_visited(True)
    if cell.get_bottom_corner() == self.__exit_corner:
      return True
    while True:
      neighbors = self.__get_unvisited_neighbors(row, col)
      if len(neighbors) == 0:
        return False
      for neighbor in neighbors:
          neighbor_cell = self.get_cell(neighbor[0], neighbor[1])
          if (neighbor[0] == row - 1 and neighbor[1] == col and not neighbor_cell.get_bottom_wall() and not cell.get_top_wall()) or \
            (neighbor[0] == row + 1 and neighbor[1] == col and not neighbor_cell.get_top_wall() and not cell.get_bottom_wall()) or \
            (neighbor[1] == col - 1 and neighbor[0] == row and not neighbor_cell.get_right_wall() and not cell.get_left_wall()) or \
            (neighbor[1] == col + 1 and neighbor[0] == row and not neighbor_cell.get_left_wall() and not cell.get_right_wall()):
            cell.draw_move(self.window.canvas, neighbor_cell, False)
            if self.__solve_recursive(neighbor[0], neighbor[1]):
              return True
            cell.draw_move(self.window.canvas, neighbor_cell, True)
 
