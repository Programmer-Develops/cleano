import pandas as pd

def normalize_data(data):
    return (data - data.min()) / (data.max() - data.min())

def encode_categorical(data, columns):
    return pd.get_dummies(data, columns=columns, drop_first=True)

class DataPreprocessor:
    def __init__(self,data):
        self.data = data
    
    def normalize(self):
        self.data = normalize_data(self.data)
        return self.data
    
    def encode(self,columns):
        self.data = encode_categorical(self.data, columns)
        return self.data
    
    def get_data(self):
        return self.data