from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery

class Car(Serviceable):
    def __init__(self, Engine,Battery):
        self.Engine=Engine
        self.Battery=Battery
    
    def needs_service(self):
        if(self.Engine.needs_service or self.Battery.needs_service):
            return True
