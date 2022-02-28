from ChristmasLights.order import Order
from ChristmasLights.light import Light


class BehaviorOrderTurnOff(Order):
    def execute(self, light: Light):
        light.State = False

    def Name(self) -> str:
        return "TurnOff"
