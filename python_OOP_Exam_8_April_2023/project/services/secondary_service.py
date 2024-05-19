from project.services.base_service import BaseService


class SecondaryService(BaseService):
    ROBOT_TYPE = "FemaleRobot"
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"""{self.name} Secondary Service:
Robots: {self._get_names()}"""
