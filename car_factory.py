from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

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

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car