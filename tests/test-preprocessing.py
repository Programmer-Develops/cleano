import unittest
import pandas as pd
from cleano.preprocessing import DataPreprocessor, normalize_data, encode_categorical

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.Series([1, 2, 3, 4, 5])
        self.cat_data = pd.DataFrame({'animal': ['cat', 'dog', 'cat', 'bird']})
        self.preprocessor = DataPreprocessor(self.sample_data)
    
    def test_normalize_data(self):
        expected = pd.Series([0.0, 0.25, 0.5, 0.75, 1.0])
        result = normalize_data(self.sample_data)
        pd.testing.assert_series_equal(result, expected)

    def test_encode_categorical(self):
        result = encode_categorical(self.cat_data, columns=['animal'])
        expected_columns = ['animal_cat', 'animal_dog']
        for col in expected_columns:
            self.assertIn(col, result.columns)
        expected = pd.DataFrame({
            'animal_cat': [1, 0, 1, 0],
            'animal_dog': [0, 1, 0, 0]
        })
        # Convert result dtypes to int for comparison
        pd.testing.assert_frame_equal(
            result.reset_index(drop=True)[expected_columns].astype(int),
            expected
        )

if __name__ == '__main__':
    unittest.main()