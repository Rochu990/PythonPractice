import unittest
from parameterized import parameterized
from car import Car


 
   
@parameterized(
            (6, 30, 60, 10, 40),
            (7, 40, 70, 5, 45),
            (8, 25, 30, 0, 25)
    )
def test_refuel(self, combustion, tank_fuel, max_fuel, refuel, expected):
        
        car = Car(combustion, tank_fuel, max_fuel)
          
        self.assertEqual(car.refuel(refuel), expected)
        

    # def test_drive(self):
       
    #     car_1 = Car(6, 30, 60)
    #     car_2 = Car(7, 40, 70)
    #     car_3 = Car(8, 25, 30) 

    #     self.assertEqual(car_1.drive(150), 9)
    #     self.assertEqual(car_2.drive(300), 21)
    #     self.assertEqual(car_3.drive(250), 20)

    # def test_details(self):

    #     car_1 = Car(6, 30, 60)
    #     car_2 = Car(7, 40, 70)
    #     car_3 = Car(8, 25, 30) 

    #     self.assertEqual(car_1.details(), "spalanie 6 objętość baku 30")
    #     self.assertEqual(car_2.details(), "spalanie 7 objętość baku 40")
    #     self.assertEqual(car_3.details(), "spalanie 8 objętość baku 25")
   

    
if __name__ == '__main__':
    unittest.main()

