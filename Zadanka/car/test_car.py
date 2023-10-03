import unittest
from car import Car


class TestCar(unittest.TestCase):  
    def test_refuel(self):
        
        car_1 = Car(6, 30, 60)
        car_2 = Car(7, 40, 70)
        car_3 = Car(8, 25, 30)    

        self.assertEqual(car_1.refuel(10), 40)
        self.assertEqual(car_2.refuel(5), 45)
        self.assertEqual(car_3.refuel(0), 25)

    def test_drive(self):
       
        car_1 = Car(6, 30, 60)
        car_2 = Car(7, 40, 70)
        car_3 = Car(8, 25, 30) 

        self.assertEqual(car_1.drive(150), 9)
        self.assertEqual(car_2.drive(300), 21)
        self.assertEqual(car_3.drive(250), 20)

    def test_details(self):

        car_1 = Car(6, 30, 60)
        car_2 = Car(7, 40, 70)
        car_3 = Car(8, 25, 30) 

        self.assertEqual(car_1.details(), "spalanie 6 objętość baku 30")
        self.assertEqual(car_2.details(), "spalanie 7 objętość baku 40")
        self.assertEqual(car_3.details(), "spalanie 8 objętość baku 25")
   

    
if __name__ == '__main__':
    unittest.main()

