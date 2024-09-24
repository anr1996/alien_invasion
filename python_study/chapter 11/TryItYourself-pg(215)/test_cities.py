import unittest 
from city_functions import My_location_details

class NameTestCase(unittest.TestCase):
    """Tests for MY_location_details"""
    def test_city_country(self):
        """use info like city and country names"""
        person_city_country = My_location_details('Santiago', 'Chile')
        self.assertEqual(person_city_country, 'Santiago Chile')

if __name__ == '__main__':
    unittest.main()