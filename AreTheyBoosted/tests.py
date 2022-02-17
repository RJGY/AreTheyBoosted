import unittest
import sys
import os
sys.path.append(os.getcwd() + '\\api')
import api


class TestMatchAPIMethods(unittest.TestCase):
    def test_get_match_no_params(self):
        self.assertEqual(api.match.get_match_ids(), None)

    def test_get_match_only_region_param(self):
        self.assertEqual(api.match.get_match_ids(None, "Oceania"), None)

    def test_get_match_only_name_param(self):
        self.assertEqual(api.match.get_match_ids("Reese", None), None)

    def test_get_match_only_incorrect_name_param(self):
        self.assertEqual(api.match.get_match_ids("Re", "Oceania"), None)

    def test_get_match_only_incorrect_region_param(self):
        self.assertEqual(api.match.get_match_ids("Reese", "Oc"), None)


if __name__ == '__main__':
    unittest.main()