from ChristmasLights.order import Order
from ChristmasLights.light import Light


class BehaviorOrderToggle(Order):
    def execute(self, light: Light):
        light.State = not light.State

    def Name(self) -> str:
        return "Toggle"
