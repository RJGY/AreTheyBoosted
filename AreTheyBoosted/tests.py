import unittest
from api import get_match

class TestAPIMethods(unittest.TestCase):
    def test_get_match(self):
        self.assertEqual(get_match.get_match_ids(), None)


if __name__ == '__main__':
    unittest.main()