class NubbinBattery(Battery):
    def needs_service(self):
        return (self.current_date.year - self.last_service_date.year) >= 4
