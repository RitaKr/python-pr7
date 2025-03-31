import unittest
from app.io.input import read_file
import os

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        #creating sample files for testing
        self.text_file_path = '../../data/test_example.txt'
        with open(self.text_file_path, 'w') as f:
            f.write('some text here!')


    def tearDown(self):
        # Remove the sample files
        os.remove(self.text_file_path)

    def test_read_file(self):
        content = read_file(self.text_file_path)
        self.assertEqual(content, 'some text here!')

    def test_read_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file('../../data/nonexistent.txt')

    def test_read_file_empty(self):
        empty_file_path = '../../data/empty.txt'
        with open(empty_file_path, 'w') as f:
            pass
        content = read_file(empty_file_path)
        self.assertEqual(content, '')
        os.remove(empty_file_path)

if __name__ == '__main__':
    unittest.main()