#!/usr/bin/env python3

"""
Stanford CS106A TextGrid
YOU SHOULD NOT MODIFY THIS FILE.
Written by Miranda Li and Patricia Wei.
TextGrid Features:
Create grid:
  grid = TextGrid.blank(400, 200)   # create new grid of size
  grid = TextGrid('foo.txt')        # create from file
Access size
  grid.width, grid.height
Get cell at x,y
  cell = grid.get_cell(x, y)
Set cell at x,y with Cell object
  grid.set_cell(x, y, cell)   # set data by tuple also
Set cell at x,y with character value
  grid.set_value(x, y, value)   # set data by tuple also
Print cell to console
  cell.show()
The main() function below demonstrates the above functions as a test.
"""
import sys

class Cell(object):
    """
    A single character at an x,y in a TextGrid
    Supports set/get .value
    """
    def __init__(self, value, x, y):
        self.value = value
        self._x = x
        self._y = y

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.getter
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise Exception(f'New value must be a string')
        if len(new_value) != 1:
            raise Exception(f'New value must be of length 1')
        self._value = new_value.upper()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class TextGrid(object):
    def __init__(self, filename, width=0, height=0):
        """
        Create a new grid from a text file. This case works: TextGrid('foo.txt')
        To create a blank grid use TextGrid.blank(2, 2)
        """
        if filename:
            data = []
            with open(filename) as f:
                for y, line in enumerate(f.readlines()):
                    row = []
                    for x, char in enumerate(line.strip()):
                        row.append(Cell(char, x, y))
                    data.append(row)
            self._data = data
            self._filename = filename  # hold onto
        else:
            if width <= 0 or height <= 0:
                raise Exception('Creating blank TextGrid requires width/height but got {} {}'
                                .format(width, height))
            data = []
            for y in range(height):
                row = [Cell('_', x, y) for x in range(width)]
                data.append(row)
            self._data = data
        self._width = len(self._data[0])
        self._height = len(self._data)
        self.curr_x = 0
        self.curr_y = 0

    def __str__(self):
        temp = ''
        for line in self._data:
            temp += (''.join([str(cell) for cell in line]))
            temp += '\n'
        return temp.strip()

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_x < self.width and self.curr_y < self.height:
            x = self.curr_x
            y = self.curr_y
            self.increment_curr_counters()
            return self._data[y][x]
        else:
            self.curr_x = 0
            self.curr_y = 0
            raise StopIteration()

    def increment_curr_counters(self):
        self.curr_x += 1
        if self.curr_x == self.width:
            self.curr_x = 0
            self.curr_y += 1

    @classmethod
    def blank(cls, width, height):
        """Create a new blank grid of the given width and height (will be populated with Cell objects with value = '_')."""
        return TextGrid('', width, height)

    @classmethod
    def file(cls, filename):
        """Create a new grid based on a file, alternative to raw constructor."""
        return TextGrid(filename)

    @property
    def width(self):
        """Width of grid (number of characters in a line)."""
        return self._width

    @property
    def height(self):
        """Height of grid (number of lines)."""
        return self._height

    def get_cell(self, x, y):
        """
        Returns a Cell at the given x,y
        """
        if x < 0 or x >= self._width or y < 0 or y >= self.height:
            e = Exception('get_cell bad coordinate x %d y %d (vs. width %d height %d)' %
                          (x, y, self._width, self._height))
            raise e
        return self._data[y][x]

    def set_cell(self, x, y, cell):
        """
        Sets cell at position (x,y) to Cell object `cell`
        """
        if x < 0 or x >= self._width or y < 0 or y >= self.height:
            e = Exception('set_cell bad coordinate x %d y %d (vs. width %d height %d)' %
                          (x, y, self._width, self.height))
            raise e
        self._data[y][x].value =  cell.value


def main():
    """
    main() exercises the features as a test.
    1. With 1 arg like small_genome.txt - opens it and prints to console
    2. With 2 args (width then height), creates a blank grid of input dimensions and prints to console
    3. With 0 args, creates blank 4x4 grid.
    """
    args = sys.argv[1:]

    if len(args) == 1:
        grid = TextGrid.file(args[0])
        print(grid)
        return

    if len(args) == 2:
        grid = TextGrid.blank(int(args[0]), int(args[1]))
        print(grid)
        return

    grid = TextGrid.blank(4,4)
    print(grid)

if __name__ == '__main__':
    main()

