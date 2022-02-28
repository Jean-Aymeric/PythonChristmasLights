from ChristmasLights.lightsArray import LightsArray
from ChristmasLights.instruction import Instruction
from ChristmasLights.grid import Grid
from ChristmasLights.orders import Orders

lights: LightsArray
orders: Orders

lights = LightsArray(1000, 1000)
orders = Orders()
Instruction(Grid(887, 9, 959, 629), orders.get("TurnOn")).execute(lights)
Instruction(Grid(454, 398, 844, 448), orders.get("TurnOn")).execute(lights)
Instruction(Grid(539, 243, 559, 965), orders.get("TurnOff")).execute(lights)
Instruction(Grid(370, 819, 676, 868), orders.get("TurnOff")).execute(lights)
Instruction(Grid(145, 40, 370, 997), orders.get("TurnOff")).execute(lights)
Instruction(Grid(301, 3, 808, 453), orders.get("TurnOff")).execute(lights)
Instruction(Grid(351, 678, 951, 908), orders.get("TurnOn")).execute(lights)
Instruction(Grid(720, 196, 897, 994), orders.get("Toggle")).execute(lights)
Instruction(Grid(831, 394, 904, 860), orders.get("Toggle")).execute(lights)
print(lights.count())
