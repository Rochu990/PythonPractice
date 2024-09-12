from test_base import BaseTestCase

class CarTest(BaseTestCase):
    def test_get_car(self):
        response = self.client.get('/car/1')
        self.assert200(response)
        self.assertEqual(response.json, {
            'combustion': 13,
            'id': 1,
            "max_fuel": 45,
            "tank_fuel": 28
        })