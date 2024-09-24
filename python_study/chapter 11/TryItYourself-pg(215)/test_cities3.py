import unittest
from city_functions3 import My_location_details

class TestNameCase(unittest.TestCase):
    """Test function My_location_details"""

    def test_city_country_population(self):

        """option arguments 2 or 3 """
        """city, country, population
        or city country,"""
        
        population_location = My_location_details('chile', 'santiago', '10_000')
        self.assertEqual(population_location, 'Chile Santiago 10_000')


if __name__ == '__main__':
    unittest.main()
        

    
