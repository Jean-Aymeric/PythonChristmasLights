from ChristmasLights.grid import Grid
from ChristmasLights.order import Order
from ChristmasLights.lightsArray import LightsArray


class Instruction:
    __grid: Grid
    __order: Order

    def __init__(self, grid: Grid, order: Order):
        self.__grid = grid
        self.__order = order

    def execute(self, lights: LightsArray):
        for y in range(self.__grid.Y1, self.__grid.Y2 + 1):
            for x in range(self.__grid.X1, self.__grid.X2 + 1):
                self.__order.execute(lights.getLightXY(x, y))
