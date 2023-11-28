import unittest
from transmiters import point, transmiter_range, range_path

t1 = (6, 11, 4)
t2 = (8, 17, 3)
t3 = (19, 19, 2)
t4 = (19, 11, 4)
t5 = (15, 7, 6)
t6 = (12, 19, 4)

transmiters =  [t1, t2, t3, t4, t5, t6]

class TestTtansmiters(unittest.TestCase):
    def test_point(self):
        self.assertEqual(point((14, 55), transmiters), [])
        self.assertEqual(point((18, 12), transmiters), [t4, t5])
        self.assertEqual(point((18, 18), transmiters), [t3])

    def test_transmiter_range(self):
        self.assertEqual(transmiter_range((2,2,1), (3,3,1)), True)
        self.assertEqual(transmiter_range((3,3,1), (4,2,1)), True)
        self.assertEqual(transmiter_range((2,2,1), (5,2,1)), False)

    def test_range_path(self):
        self.assertEqual(range_path([t1, t2, t3, t4, t5, t6]), [t1, t2, t5, t6, t4])
     

if __name__ == '__main__':
    unittest.main()