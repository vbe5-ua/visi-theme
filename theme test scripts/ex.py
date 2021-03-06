# code from the Sample Programs in Every Language (SPEL) project 

from random import randint

class Cell:
    def __init__(self):
        self._status = 'Dead'

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        if self._status == 'Alive':
            return True
        return False

    def get_print_character(self):
        if self.is_alive():
            return 'O'
        return '.'

class Board:
    def __init__(self, rows):
        self._rows = rows
        self._grid = [[Cell() for _ in range(self._columns)] for _ in range(self._rows)]
        self._generate_board()
                    
    def draw_board(self):
        print('\n' * 10)
        print('printing board')
        for row in self._grid:
            for column in row:
                print(column.get_print_character(), end='')
            print()  # to create a new line pr. row.

    def update_board(self):
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                check_neighbour = self.check_neighbour(row, column)
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)
                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)
                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # sett cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    def check_neighbour(self, check_row, check_column):
        # how deep the search is:
        search_min = -1
        search_max = 2

        # empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_column:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self._rows:
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(
                        self._grid[neighbour_row][neighbour_column])
        return neighbour_list


def main():
    # assume the user types in a number
    user_rows = int(input('how many rows? '))
    user_columns = int(input('how many columns? '))

    # create a board:
    game_of_life_board = Board(user_rows, user_columns)

    # run the first iteration of the board:
    game_of_life_board.draw_board()
    # game_of_life_board.update_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


main()