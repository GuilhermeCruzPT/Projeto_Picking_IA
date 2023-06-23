import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        # TODO (rever)
        self.line_forklift = None
        self.column_forklift = None
        self.line_exit = None
        self.column_forklift = None

        self.rows = rows
        self.columns = columns
        self.matrix = np.full([self.rows, self.columns], fill_value=0, dtype=int)

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = matrix[i][j]
                if self.matrix[i][j] == constants.FORKLIFT:
                    self.line_forklift = i
                    self.column_forklift = j
                if self.matrix[i][j] == constants.EXIT:
                    self.line_exit = i
                    self.column_exit = j

    def can_move_up(self) -> bool:
        # TODO (rever)
        return self.line_forklift != 0 and \
            self.matrix[self.line_forklift - 1][self.column_forklift] != constants.SHELF and \
            self.matrix[self.line_forklift - 1][self.column_forklift] != constants.PRODUCT and \
            self.matrix[self.line_forklift - 1][self.column_forklift] != constants.PRODUCT_CATCH

    def can_move_right(self) -> bool:
        # TODO (rever)
        return self.column_forklift != self.columns - 1 and \
            self.matrix[self.line_forklift][self.column_forklift + 1] != constants.SHELF and \
            self.matrix[self.line_forklift][self.column_forklift + 1] != constants.PRODUCT and \
            self.matrix[self.line_forklift][self.column_forklift + 1] != constants.PRODUCT_CATCH

    def can_move_down(self) -> bool:
        # TODO (rever)
        return self.line_forklift != self.rows - 1 and \
            self.matrix[self.line_forklift + 1][self.column_forklift] != constants.SHELF and \
            self.matrix[self.line_forklift + 1][self.column_forklift] != constants.PRODUCT and \
            self.matrix[self.line_forklift + 1][self.column_forklift] != constants.PRODUCT_CATCH

    def can_move_left(self) -> bool:
        # TODO (rever)
        return self.column_forklift != 0 and \
            self.matrix[self.line_forklift][self.column_forklift - 1] != constants.SHELF and \
            self.matrix[self.line_forklift][self.column_forklift - 1] != constants.PRODUCT and \
            self.matrix[self.line_forklift][self.column_forklift - 1] != constants.PRODUCT_CATCH

    # In the next four methods we don't verify if the actions are valid.
    # This is done in method getActions in class WarehouseProblemSearch.
    # Doing the verification in these methods would imply that a clone of the
    # state was created whether the operation could be executed or not.

    def move_up(self) -> None:
        # TODO (rever)
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift -= 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_right(self) -> None:
        # TODO (rever)
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift += 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_down(self) -> None:
        # TODO (rever)
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift += 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_left(self) -> None:
        # TODO (rever)
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift -= 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def get_cell_color(self, row: int, column: int) -> Color:
        if row == self.line_exit and column == self.column_exit and (
                row != self.line_forklift or column != self.column_forklift):
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return np.array_equal(self.matrix, other.matrix)
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
