class Light:
    __state: bool

    def __init__(self):
        self.__state = False

    @property
    def State(self) -> bool:
        return self.__state

    @State.setter
    def State(self, state: bool) -> None:
        self.__state = state
