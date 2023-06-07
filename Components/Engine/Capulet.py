from Components.Engine import Engine

class Capulet(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 30000
