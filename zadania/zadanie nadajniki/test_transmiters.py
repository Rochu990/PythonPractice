import unittest

from transmiters import (
    Point,
    Transmiter,
    signal_range,
    transmiter_range,
)


class TestSignal(unittest.TestCase):
    def test_transmiter_range(self):
        self.assertEqual(
            transmiter_range(Transmiter(2, 2, 1), Transmiter(3, 3, 1)), True
        )
        self.assertEqual(
            transmiter_range(Transmiter(3, 3, 1), Transmiter(4, 2, 1)), True
        )
        self.assertEqual(
            transmiter_range(Transmiter(2, 2, 1), Transmiter(5, 2, 1)), False)

    def test_solution_where_sets_dont_intersect(self):
        transmiters = [
            Transmiter(0, 0, 1),
            Transmiter(0, 1, 1),
            Transmiter(0, 2, 1),
            Transmiter(0, 3, 1),
            Transmiter(0, 4, 1),
            Transmiter(0, 5, 1),
            Transmiter(10, 10, 1),
            Transmiter(10, 11, 1),
            Transmiter(10, 12, 1),
            Transmiter(10, 13, 1),
            Transmiter(10, 14, 1),
            Transmiter(10, 15, 1),
        ]
        start = Point(0, 0)
        end = Point(10, 10)
        self.assertFalse(signal_range(start, end, transmiters))


if __name__ == "__main__":
    unittest.main()
