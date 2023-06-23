from WarehouseProject_TODO.warehouse.cell import Cell


class Pair:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        self.value = 0
        # TODO (rever)
        self.path = []

    # TODO (rever)
    def add_cell_to_path(self, line, column):
        self.path.append(Cell(line, column))

    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __str__(self):
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(self.cell2.column) + ": " + str(self.value) + "\n"

