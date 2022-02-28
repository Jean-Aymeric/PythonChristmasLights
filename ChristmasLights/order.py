from abc import ABC, abstractmethod
from ChristmasLights.light import Light


class Order(ABC):
    @abstractmethod
    def execute(self, light: Light) -> None:
        ...

    @abstractmethod
    def Name(self) -> str:
        ...
