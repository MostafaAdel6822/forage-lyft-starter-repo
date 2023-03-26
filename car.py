from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tyres.tyres import Tyres
class Car(Serviceable):
    def __init__(self, Engine,Battery,Tyres):
        self.Engine=Engine
        self.Battery=Battery
        self.Tyres=Tyres
    
    def needs_service(self):
        if(self.Engine.needs_service or self.Battery.needs_service):
            return True
