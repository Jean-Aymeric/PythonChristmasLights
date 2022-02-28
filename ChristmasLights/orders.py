from ChristmasLights.behaviorOrder.behaviorOrderTurnOn import BehaviorOrderTurnOn
from ChristmasLights.behaviorOrder.behaviorOrderTurnOff import BehaviorOrderTurnOff
from ChristmasLights.behaviorOrder.behaviorOrderToggle import BehaviorOrderToggle
from ChristmasLights.order import Order
from ChristmasLights.light import Light


class Orders:
    __behaviorOrders: [Order]

    def __init__(self):
        self.__behaviorOrders = []
        self.__behaviorOrders.append(BehaviorOrderTurnOn())
        self.__behaviorOrders.append(BehaviorOrderTurnOff())
        self.__behaviorOrders.append(BehaviorOrderToggle())

    def get(self, orderName: str) -> Order:
        for order in self.__behaviorOrders:
            if order.Name() == orderName:
                return order
        return None
