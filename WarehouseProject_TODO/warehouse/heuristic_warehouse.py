from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # TODO (rever)
        return abs(state.line_exit - state.line_forklift) + abs(state.column_exit - state.column_forklift)

    def __str__(self):
        return "Manhattan distance to goal position"

