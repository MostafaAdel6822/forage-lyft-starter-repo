from abc import ABC, abstractmethod
from engine import capulet_engine
class CarFactory(ABC):
    def create_calliope(self):
        return Car(capulet_engine(),Battery())
    
    def create_glissade():
        return Car()
    
    def create_palindrome():
        return Car()
    
    def create_rorschach():
        return Car()
    
    def create_thovex():
        return Car()