# Adding New Tests
import unittest
from name_function3 import get_formatted_name



class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


    def test_first_last_name_middle(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
 



if __name__ == '__main__':
    unittest.main()
