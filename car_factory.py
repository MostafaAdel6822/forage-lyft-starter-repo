from abc import ABC, abstractmethod
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.engine import Engine
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
class CarFactory:
    @staticmethod
    def  create_calliope(self, current_mileage, last_service_mileage, current_date, last_service_date) -> Car:
        return  Car(CapuletEngine(current_mileage,last_service_mileage),SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_glissade(self, current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_palindrome(self, warning_light_is_on, last_service_date, current_date) -> Car:
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_rorschach(self,current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(last_service_date, current_date))
    
    @staticmethod
    def create_thovex(self, current_mileage,last_service_mileage, last_service_date, current_date) -> Car:
        return Car(CapuletEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date, current_date))