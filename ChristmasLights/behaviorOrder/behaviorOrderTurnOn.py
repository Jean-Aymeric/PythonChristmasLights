from ChristmasLights.order import Order
from ChristmasLights.light import Light


class BehaviorOrderTurnOn(Order):
    def execute(self, light: Light):
        light.State = True

    def Name(self) -> str:
        return "TurnOn"
