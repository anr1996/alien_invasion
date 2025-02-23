import unittest
from city_functions import location


class NamesTestCase(unittest.TestCase):
    

    def test_city_country(self):
        "verify the function location is working correctly"
        
        formatted_loc = location('Chicago', 'United States')
        self.assertEqual(formatted_loc, 'Chicago United States')
        
if __name__ == '__main__':
    unittest.main()
    
        

    