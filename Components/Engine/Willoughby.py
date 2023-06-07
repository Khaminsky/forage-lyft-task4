from Components.Engine import Engine

class Willoughby(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 60000
