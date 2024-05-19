from project.services.base_service import BaseService


class MainService(BaseService):
    ROBOT_TYPE = "MaleRobot"
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"""{self.name} Main Service:
Robots: {self._get_names()}"""
