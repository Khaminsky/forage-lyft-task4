from Components.Battery import Battery

class SpindlerBattery(Battery):
    def needs_service(self):
        return (self.current_date.year - self.last_service_date.year) >= 2
