from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    _TYPE = "FemaleRobot"
    INITIAL_WEIGHT = 7
    INCREASE_WEIGHT = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += self.INCREASE_WEIGHT
