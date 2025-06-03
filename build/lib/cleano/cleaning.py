import pandas as pd

def remove_dup(data):
    return data.drop_duplicates()

def fill_missing_val(data, strategy = "mean",  fill_value = None):
    if strategy == "mean":
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])
    elif strategy == 'constant':
        return data.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy")
    
class DataCleaner:
    def __init__(self,data):
        self.data = data

    def clean(self):
        self.data = remove_dup(self.data)
        self.data = fill_missing_val(self.data)
        return self.data