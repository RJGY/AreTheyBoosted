import unittest
from api import get_match

class TestGetMatchAPIMethods(unittest.TestCase):
    def get_match_no_params(self):
        self.assertEqual(get_match.get_match_ids(), None)

    def get_match_only_region_param(self):
        self.assertEqual(get_match.get_match_ids(), None)

    def get_match_only_name_param(self):
        self.assertEqual(get_match.get_match_ids(), None)


if __name__ == '__main__':
    unittest.main()