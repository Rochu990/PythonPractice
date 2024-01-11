import unittest
from plecak2 import backpack, Item

class TestBackPack(unittest.TestCase):
    # 1 -> nazwa funkcji
    # 2 -> zmienne tworz w funkcji a nie w klasie
    # 3 ->
    #   a) item tworzysz przez Item(1, 10, "nazwa") lub Item(value=1, weight=2, name="qwe")
    #   b) to co zrobiłeś to zmieniłeś atrybuty klasy.
    #      Zapoznaj się z tym: https://ddeby.pl/blog/10-nietypowych-zachowan-w-python#atrybuty_klasowe
    # 4 -> zawsze dodawaj 2 funkcje -> pomoze Ci to zeby nie wpasc w pułapke jak wczesniej
    def test_backpack_should_be_empty_when_capacity_is_lower_than_all_items(self):
        items = [Item(10, 10, "ring")]
        capacity = 5
        self.assertEqual(backpack(items, capacity), [])
 
    def test_backpack_should_be_empty_when_there_is_no_items(self):
        items = []
        capacity = 5
        self.assertEqual(backpack(items, capacity), [])
    
    def test_bp_1_item(self):
        items = [Item(10, 10, "ring")]
        capacity = 10
        self.assertEqual(backpack(items, capacity), items)

    def test_bp_2_item(self):
        item =Item(10, 10, "ring")
        capacity = 20
        self.assertEqual(backpack([item], capacity), [item, item])
    
    def test_bp_3_item(self):
        ring  = Item(10, 10, "ring")
        zegarek = Item(5, 4, "zegarek")
        capacity = 15
        self.assertEqual(backpack([ring, zegarek], capacity), [ring, zegarek])

    def test_bp_3_item(self):
        ring  = Item(10, 10, "ring")
        zegarek = Item(5, 4, "zegarek")
        capacity = 11
        self.assertEqual(backpack([ring, zegarek], capacity), [ring])
        
    def test_bp_3_item(self):
        ring  = Item(10, 10, "ring")
        zegarek = Item(5, 10, "zegarek")
        capacity = 10
        self.assertEqual(backpack([ring, zegarek], capacity), [zegarek, zegarek])
 
 
if __name__ == '__main__':
    unittest.main()