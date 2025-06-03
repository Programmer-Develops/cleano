def is_null(value):
    return value is None or (isinstance(value, float) and value != value)

def validate_data(data):
    if not isinstance(data, (list,dict)):
        raise TypeError("Data must be a list or dictionary")
    return True

def log_meggage(message):
    print(f"LOG: {message}")