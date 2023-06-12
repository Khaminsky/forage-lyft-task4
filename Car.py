from engine import Engine
from battery import Battery
from datetime import datetime

class Car:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self) -> bool:
        service_threshold_date = self.engine.last_service_date.replace(year=self.engine.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.needs_service():
            return True
        else:
            return False
