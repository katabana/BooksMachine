import unittest
import json
from checker import search_json


class TestSearchJson(unittest.TestCase):
    def test_search_json(self):
        f = open('res.json')
        data = f.read()
        f.close()
        data = json.loads(data)
        res = search_json(data)

        self.assertEqual(res[0], {'title': "Opium w rosole", 'subtitle': None, 'authors': ["Małgorzata Musierowicz"]})

        self.assertEqual(res[1], {'title': "Humor i komizm językowy w wybranych powieściach Małgorzaty Musierowicz",
                                  'subtitle': None, 'authors': ["Halina Maczunder"]})

        self.assertEqual(res[2], {'title': "Poznań Borejków",
                                  'subtitle': "spacer z bohaterami powieści Małgorzaty Musierowicz",
                                  'authors': ["Małgorzata Musierowicz"]})

        self.assertEqual(res[8], {'title': "W poszukiwaniu nowych rozwiązań",
                                  'subtitle': "Dydaktyka języka polskiego jako obcego u progu XXI wieku",
                                  'authors': ["Władysław T. Miodunka", "Anna Seretny"]})


if __name__ == '__main__':
    unittest.main()
