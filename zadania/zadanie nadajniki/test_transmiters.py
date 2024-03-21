import unittest
from transmiters import point, transmiter_range, range_path, solution

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
        self.assertEqual(range_path(transmiters), {(6, 11, 4), (19, 19, 2), (12, 19, 4), (19, 11, 4), (8, 17, 3), (15, 7, 6)})

    def test_start_nie_znajduje_sie_w_zadnym_radarze(self):
        start = (-10, -80)
        end = (19, 14)
        
        self.assertFalse(solution(start, end, transmiters))

    def test_end_nie_znajduje_sie_w_zadnym_radarze(self):
        start = (0, 0)
        end = (42, 55)
        
        self.assertFalse(solution(start, end, transmiters))
    
    def test_start_i_end_w_tym_samym_punkcie(self):
        start = (19, 14)
        end = (19, 14)
        self.assertTrue(solution(start, end, transmiters))

    # def test_range_path(self):
    #     self.assertEqual(range_path([t1, t2, t3, t4, t5, t6]), [t1, t2, t5, t6, t4])
    
    # def test_solution_kiedy_zbiory_sie_nie_przecinaja(self):
    #     transmiters = [(0, 0, 1),
    #         (0, 1, 1),
    #         (0, 2, 1),
    #         (0, 3, 1),
    #         (0, 4, 1),
    #         (0, 5, 1),
    #         (10, 10, 1),
    #         (10, 11, 1),
    #         (10, 12, 1),
    #         (10, 13, 1),
    #         (10, 14, 1),
    #         (10, 15, 1)]
    #     start = (0, 0)
    #     end = (10, 10)
    #     self.assertFalse(solution(start, end, transmiters))


if __name__ == '__main__':
    unittest.main()