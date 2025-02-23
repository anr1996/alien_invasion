import unittest
from location_functions import location_population


class NamesTestCase(unittest.TestCase):
    

    def test_city_location_population(self):
        "verify the function location is working correctly"
        
        formatted_loc = location_population('Chicago', 'United States')
        self.assertEqual(formatted_loc, 'Chicago United States')
        
        
    def test_city_location_population_2(self):
        "Verify the function location and population is working correctly"
        
        formatted_loc = location_population('Chicago', 'United States', 'population 1000000')
        self.assertEqual(formatted_loc, ('Chicago United States population 1000000'))
        
if __name__ == '__main__':
    unittest.main()
    
        

    