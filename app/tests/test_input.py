import unittest
from app.io.input import read_file, read_file_pandas
import pandas as pd
import os

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        #creating sample files for testing
        self.text_file_path = '../../data/test_example.txt'
        with open(self.text_file_path, 'w') as f:
            f.write('some text here!')

        self.csv_file_path = '../../data/test_example.csv'
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df.to_csv(self.csv_file_path, index=False)

    def tearDown(self):
        os.remove(self.text_file_path)
        os.remove(self.csv_file_path)

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

    def test_read_file_pandas(self):
        df = read_file_pandas(self.csv_file_path)
        expected_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_read_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas('../../data/nonexistent.csv')

    def test_read_file_pandas_empty(self):
        empty_csv_path = '../../data/empty.csv'
        pd.DataFrame().to_csv(empty_csv_path, index=False)
        with self.assertRaises(pd.errors.EmptyDataError):
            read_file_pandas(empty_csv_path)

if __name__ == '__main__':
    unittest.main()