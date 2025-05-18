import pandas as pd
import os

def load_data(path='data/defects.csv'):
    df = pd.read_csv(path)
    print("Data Shape:", df.shape)
    return df

def preprocess_data(df):
    # Handle missing values
    df = df.dropna()
    
    # Encode labels if needed
    if 'defect_type' in df.columns:
        df['defect_type'] = df['defect_type'].astype('category').cat.codes

    return df

if __name__ == "__main__":
    df = load_data()
    df = preprocess_data(df)
    df.to_csv("data/cleaned_data.csv", index=False)