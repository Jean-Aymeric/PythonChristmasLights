from ChristmasLights.light import Light


class LightsArray:
    __width: int
    __height: int
    __lights: [[Light]]

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__lights = [[None] * width for i in range(height)]
        for y in range(self.__height):
            for x in range(self.__width):
                self.__lights[y][x] = Light()

    @property
    def Width(self) -> int:
        return self.__width

    @property
    def Height(self) -> int:
        return self.__height

    def getLightXY(self, x: int, y: int) -> Light:
        return self.__lights[y][x]

    def count(self) -> int:
        count = 0
        for y in range(self.__height):
            for x in range(self.__width):
                count += self.getLightXY(x, y).State
        return count
