# a failing Test
import unittest
from name_function3 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis', 'Joplin', 'Joe')
        self.assertEqual(formatted_name, 'Janis Joe Joplin')

if __name__ == '__main__':
    unittest.main()
