from abc import ABC, abstractmethod
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from engine.engine import Engine
from engine.car import Car
from engine.battery import spindler_battery
from engine.battery import nubbin_battery
class CarFactory(ABC):
    def  create_calliope(self, current_mileage, last_service_mileage, current_date, last_service_date) -> Car:
        return  Car(capulet_engine(current_mileage,last_service_mileage),spindler_battery(last_service_date, current_date))
    
    def create_glissade(self, current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        return Car(willoughby_engine(current_mileage, last_service_mileage),spindler_battery(last_service_date, current_date))
    
    def create_palindrome(self, warning_light_is_on, last_service_date, current_date) -> Car:
        return Car(sternman_engine(warning_light_is_on),spindler_battery(last_service_date, current_date))
    
    def create_rorschach(self,current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        return Car(willoughby_engine(current_mileage, last_service_mileage),nubbin_battery(last_service_date, current_date))
    
    def create_thovex(self, current_mileage,last_service_mileage, last_service_date, current_date) -> Car:
        return Car(capulet_engine(current_mileage,last_service_mileage),nubbin_battery(last_service_date, current_date))