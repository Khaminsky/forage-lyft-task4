from Components.Engine import Willoughby, Sternman, Capulet
from Components.Battery import SpindlerBattery, NubbinBattery
from Car import Calliope, Palindrome, Glissade, Rorschach, Thovex

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date, current_date, last_service_mileage, current_mileage):
        engine = Capulet(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Calliope(engine, battery)

    @staticmethod
    def create_palindrome(last_service_date, current_date, last_service_mileage, current_mileage):
        engine = Sternman(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Palindrome(engine, battery)

    @staticmethod
    def create_glissade(last_service_date, current_date, last_service_mileage, current_mileage):
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
