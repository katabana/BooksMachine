import unittest
from checker import compare_author


class TestCompareAuthor(unittest.TestCase):
    def test_compare_author(self):
        res = compare_author({'title': None, 'subtitle': None, 'authors': [None]}, 'Michail Bulhakov')
        self.assertEqual(res, False)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Michail']}, 'Michail Bulhakov')
        self.assertEqual(res, False)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Michail', 'Gustav Bulhakov']},
                             'Michail Bulhakov')
        self.assertEqual(res, False)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Michail Bulhakov']}, 'Michail Bulhakov')
        self.assertEqual(res, True)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['', 'Michail Bulhakov']}, 'Michail Bulhakov')
        self.assertEqual(res, True)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Michail Bulhakov']}, 'Michail')
        self.assertEqual(res, True)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Michail Bulhakov']}, 'Bulhakov')
        self.assertEqual(res, True)

        res = compare_author({'title': None, 'subtitle': None, 'authors': ['Ernest Hemingway',
                                                                           'Michail Bulhakov']}, 'Bulhakov')
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
