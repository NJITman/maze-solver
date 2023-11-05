from __future__ import annotations
from tkinter import Tk, BOTH, Canvas
from time import sleep

class Point:
  def __init__(self, x:int, y:int) -> None:
    self.x = x
    self.y = y


class Line:
  def __init__(self, point1:Point, point2:Point) -> None:
    self.__point1 = point1
    self.__point2 = point2

  def draw(self, canvas:Canvas, fill_color:str) -> None:
    canvas.create_line(self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=fill_color, width=1)
    canvas.pack(fill=BOTH, expand=1)


class Cell:
  def __init__(self, point1:Point, point2:Point, has_left_wall:bool, has_right_wall:bool, has_top_wall:bool, has_bottom_wall:bool) -> None:
    self.__point1 = point1
    self.__point2 = point2
    self.__has_left_wall = has_left_wall
    self.__has_right_wall = has_right_wall
    self.__has_top_wall = has_top_wall
    self.__has_bottom_wall = has_bottom_wall
    self.__visited = False

  def draw(self, canvas:Canvas, fill_color:str) -> None:
    canvas.create_line(self.__point1.x, self.__point1.y, self.__point1.x, self.__point2.y, fill=(fill_color if self.__has_left_wall else "white"), width=1)  
    canvas.create_line(self.__point2.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=(fill_color if self.__has_right_wall else "white"), width=1)  
    canvas.create_line(self.__point1.x, self.__point1.y, self.__point2.x, self.__point1.y, fill=(fill_color if self.__has_top_wall else "white"), width=1)
    canvas.create_line(self.__point1.x, self.__point2.y, self.__point2.x, self.__point2.y, fill=(fill_color if self.__has_bottom_wall else "white"), width=1)
    canvas.pack(fill=BOTH, expand=1)

  def get_top_corner(self) -> Point:
    return self.__point1
  
  def get_bottom_corner(self) -> Point:
    return self.__point2
  
  def get_left_wall(self) -> bool:
    return self.__has_left_wall

  def get_right_wall(self) -> bool:
    return self.__has_right_wall

  def get_top_wall(self) -> bool:
    return self.__has_top_wall

  def get_bottom_wall(self) -> bool:
    return self.__has_bottom_wall

  def set_left_wall(self, has_left_wall:bool) -> None:
    self.__has_left_wall = has_left_wall

  def set_right_wall(self, has_right_wall:bool) -> None:
    self.__has_right_wall = has_right_wall

  def set_top_wall(self, has_top_wall:bool) -> None:
    self.__has_top_wall = has_top_wall

  def set_bottom_wall(self, has_bottom_wall:bool) -> None:
    self.__has_bottom_wall = has_bottom_wall

  def get_visited(self) -> bool:
    return self.__visited

  def set_visited(self, has_visited:bool) -> None:
    self.__visited = has_visited

  def is_exit(self) -> bool:
    return self.__point1.x == self.n and self.__point1.y == 0

  def draw_move(self, canvas:Canvas, to_cell:Cell, undo:bool=False) -> None:
    fill_color = "gray" if undo else "red"
    cell_center_x = (self.__point1.x + self.__point2.x) / 2
    cell_center_y = (self.__point1.y + self.__point2.y) / 2
    to_cell_center_x = (to_cell.__point1.x + to_cell.__point2.x) / 2
    to_cell_center_y = (to_cell.__point1.y + to_cell.__point2.y) / 2
    canvas.create_line(cell_center_x, cell_center_y, to_cell_center_x, to_cell_center_y, fill=fill_color, width=1)
    canvas.pack(fill=BOTH, expand=1)


class Window:
  def __init__(self, width:int, height:int, title:str) -> None:
    self.__root = Tk()
    self.__root.title(title)
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
    self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
    self.canvas.pack(fill=BOTH, expand=1)
    self.__running = False

  def redraw(self) -> None:
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self) -> None:
    self.__running = True
    while self.__running:
      self.redraw()

  def close(self) -> None:
    self.__running = False

  def draw_line(self, line:Line, fill_color:str) -> None:
    line.draw(self.canvas, fill_color)
