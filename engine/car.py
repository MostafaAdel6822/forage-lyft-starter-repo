from abc import ABC, abstractmethod

from engine.engine import Engine
from engine.battery.battery import Battery

class Car(ABC):
    def __init__(self, Engine,Battery):
        self.Engine=Engine
        self.Battery=Battery
    
    def needs_service(self):
        if(self.Engine.needs_service or self.Battery.needs_service):
            return True
