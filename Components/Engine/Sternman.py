from Components.Engine import Engine

class Sternman(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 0  # Assuming the warning indicator will be triggered immediately
