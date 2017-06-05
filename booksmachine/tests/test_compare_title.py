import unittest
from checker import compare_title


# {'title': title, 'subtitle': subtitle, 'authors': authors}
class TestCompareTitle(unittest.TestCase):
    def test_compare_title(self):
        res = compare_title({'title': "Pan Tadeusz", 'subtitle': None, 'authors': None}, "Pan Tadeusz")
        self.assertEqual(res, True)

        res = compare_title(
            {'title': "Pan Tadeusz", 'subtitle': 'czyli ostatni zajazd na Litwie', 'authors': None},
            "Pan Tadeusz")
        self.assertEqual(res, True)

        res = compare_title({'title': "Pan", 'subtitle': 'Tadeusz', 'authors': None}, "Pan Tadeusz")
        self.assertEqual(res, True)

        res = compare_title({'title': "Pan", 'subtitle': 'Tadeusz', 'authors': None}, "Pan Wołodyjowski")
        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()
