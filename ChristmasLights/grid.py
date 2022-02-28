class Grid:
    __x1: int
    __y1: int
    __x2: int
    __y2: int

    def __init__(self,x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @property
    def X1(self):
        return self.__x1

    @property
    def Y1(self):
        return self.__y1

    @property
    def X2(self):
        return self.__x2

    @property
    def Y2(self):
        return self.__y2

