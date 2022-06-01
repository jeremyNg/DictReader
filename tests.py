import unittest

from reader import *

class Test_Reader_Class(unittest.TestCase):
    def test_reader_class(self):
        with open("test_case.csv") as file:
            reader = DictReader(file, delimiter = ",", restval = "A")
            contents = list(reader)
        try:
            self.assertCountEqual(contents,
                        [{'age': '12', 'name': 'tom', 'email': 'jeremy@test.com'},
                        {'age': '10', 'name': 'jerry', 'email': 'A'},
                        {'age': 'A', 'name': 'goffy', 'email': 'A'}])
        except AttributeError:
            # Deal with Python2, where assertCountEqual does not exist
            self.assertItemsEqual(contents,
                [{'age': '12', 'name': 'tom', 'email': 'jeremy@test.com'},
                {'age': '10', 'name': 'jerry', 'email': 'A'},
                {'age': 'A', 'name': 'goffy', 'email': 'A'}])

if __name__ == "__main__":
    unittest.main()
