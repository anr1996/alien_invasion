import unittest
from city_functions2 import My_location_details

class NameTestCase(unittest.TestCase):
    """Testing My_location_details"""

    def test_city_location_population(self):
        location_info = My_location_details('chile', 'santiago')
        self.assertEqual(location_info,'Chile Santiago 10_000')

if __name__ == '__main__':
    unittest.main()

# intentional error for practice purposes only!
# gave only two arguments for location_info.
# we needed three arguments for location_info.

