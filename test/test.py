import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery 
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestNubbin(unittest.TestCase):
    def nubbin_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)      
        test_nubbin =  NubbinBattery(last_service_date, current_date)
        self.assertTrue(test_nubbin.needs_service())

    def nubbin_needs_no_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)      
        test_nubbin =  NubbinBattery(last_service_date, current_date)
        self.assertFalse(test_nubbin.needs_service())

class TestSpindler(unittest.TestCase):
    def spindler_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)      
        test_spindler =  SpindlerBattery(last_service_date, current_date)
        self.assertTrue(test_spindler.needs_service())

    def spindler_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)      
        test_spindler =  SpindlerBattery(last_service_date, current_date)
        self.assertFalse(test_spindler.needs_service())

class TestCapulet(unittest.TestCase):
    def capulet_needs_service(self):
        test_capulet= CapuletEngine(40000,0)
        self.assertTrue(test_capulet.needs_service())

    def capulet_needs_no_service(self):
        test_capulet= CapuletEngine(20000,0)
        self.assertFalse(test_capulet.needs_service())

class TestWilloughby(unittest.TestCase):
    def willoughby_needs_service(self):
        test_willoughby= CapuletEngine(70000,0)
        self.assertTrue(test_willoughby.needs_service())

    def willoughby_needs_no_service(self):
        test_willoughby= CapuletEngine(50000,0)
        self.assertFalse(test_willoughby.needs_service())

class TestSternman(unittest.TestCase):
    def sternman_needs_service(self):
        test_sternman=SternmanEngine(True)
        self.assertTrue(test_sternman.needs_service())
    def sternman_needs_no_service(self):
        test_sternman=SternmanEngine(False)
        self.assertFalse(test_sternman.needs_service())



if __name__ == '__main__':
    unittest.main()


        

