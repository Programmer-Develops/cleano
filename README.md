# Cleano

Cleano is a Python package designed to simplify the process of data cleaning and preprocessing. It provides a set of tools that help users efficiently clean, transform, and prepare their data for analysis.

## Features

- **Data Cleaning**: Remove duplicates, fill missing values, and perform various cleaning operations with ease.
- **Data Preprocessing**: Normalize data, encode categorical variables, and prepare data for machine learning models.
- **Utility Functions**: Access helper functions for data validation and logging.

## Installation

To install the cleano package, you can use pip:

```
pip install cleano
```

## Usage

Here is a simple example of how to use the cleano package:

```python
from cleano.cleaning import DataCleaner
from cleano.preprocessing import DataPreprocessor

# Create a cleano instance
cleaner = cleano()

# Clean your data
cleaned_data = cleaner.remove_dup(data)
cleaned_data = cleaner.fill_missing_val(cleaned_data)

# Create a DataPreprocessor instance
preprocessor = DataPreprocessor()

# Preprocess your data
normalized_data = preprocessor.normalize_data(cleaned_data)
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.