import pandas as pd

def load_data(path):
    """
    Load insurance dataset from CSV file.
    
    Parameters:
        path (str): Path to dataset
        
    Returns:
        pandas.DataFrame
    """
    
    df = pd.read_csv(path)
    
    return df