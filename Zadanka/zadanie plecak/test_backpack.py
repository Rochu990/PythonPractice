import unittest
from backpack import bp, Item

class TestBackPack(unittest.TestCase):
    # 1 -> nazwa funkcji
    # 2 -> zmienne tworz w funkcji a nie w klasie
    # 3 ->
    #   a) item tworzysz przez Item(1, 10, "nazwa") lub Item(value=1, weight=2, name="qwe")
    #   b) to co zrobiłeś to zmieniłeś atrybuty klasy.
    #      Zapoznaj się z tym: https://ddeby.pl/blog/10-nietypowych-zachowan-w-python#atrybuty_klasowe
    # 4 -> zawsze dodawaj 2 funkcje -> pomoze Ci to zeby nie wpasc w pułapke jak wczesniej
    def test_backpack_should_be_empty_when_capacity_is_lower_than_all_items(self):
        items = [Item("ring", 10, 10)]
        capacity = 5
        self.assertEqual(bp(items, capacity), [])
 
    def test_backpack_should_be_empty_when_there_is_no_items(self):
        items = []
        capacity = 5
        self.assertEqual(bp(items, capacity), [])
    
    def test_bp_1_item(self):
        items = [Item("ring", 10, 10)]
        capacity = 10
        self.assertEqual(bp(items, capacity), ['ring'])

    def test_bp_2_item(self):
        item =Item("ring", 10, 10)
        capacity = 20
        self.assertEqual(bp([item], capacity), ['ring', 'ring'])
    
    def test_bp_3_item(self):
        items = [
            Item("ring", 10, 10),
            Item("zegarek", 5, 4)
        ]
        capacity = 15
        self.assertEqual(bp(items, capacity), ["ring", "zegarek"])

    def test_bp_3_item(self):
        items = [
            Item("ring", 10, 10),
            Item("zegarek", 5, 4)
        ]
        capacity = 11
        self.assertEqual(bp(items, capacity), ['ring'])
        
    def test_bp_3_item(self):
        items = [
            Item("ring", 10, 10),
            Item("zegarek", 5, 10)
        ]
        capacity = 10
        self.assertEqual(bp(items, capacity), ["zegarek", "zegarek"])
    
    def test_8_items_in_bp(self):
        items = [
            Item("zegarek", 3, 7),
            Item("bransoleta", 2, 3),
            Item("kolczyki", 1, 2)
            ]
        capacity = 20
        self.assertEqual(bp(items, capacity), ['zegarek', 'zegarek', 'zegarek', 'zegarek', 'zegarek', 'zegarek', 'kolczyki', 'kolczyki'])
 
 
if __name__ == '__main__':
    unittest.main()