import unittest
import pandas as pd
from cleano.cleaning import DataCleaner, remove_dup, fill_missing_val

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 1, "value": 10},  
            {"id": 3, "value": None},
        ]
        self.df = pd.DataFrame(self.sample_data)
        self.cleaner = DataCleaner(self.df)

    def test_remove_dup(self):
        cleaned_data = remove_dup(self.df)
        self.assertEqual(len(cleaned_data), 3)
    
    def test_fill_missing_val(self):
        filled_data = fill_missing_val(self.df, fill_value=0)
        self.assertNotIn(None, filled_data['value'].values)
        self.assertFalse(filled_data['value'].isnull().any())

if __name__ == '__main__':
    unittest.main()