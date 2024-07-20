import numpy as np
import pandas as pd
import pickle
import os
from joblib import load, dump
from sklearn.model_selection import train_test_split

def dump_pickle(obj, filename: str):
    with open(filename, "wb") as f_out:
        return pickle.dump(obj, f_out)

def read_dataframe(filename: str):
    df = pd.read_csv(filename)
    return df

def preprocess(df):
    target = "fraud"
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y

def data_prep():
    dest_path = "output"

    df = read_dataframe(os.path.join("data/", f"card_transdata.csv"))
    X, y = preprocess(df)

    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=17)
    
    # Create dest_path folder unless it already exists
    os.makedirs(dest_path, exist_ok=True)

    # Save DictVectorizer and datasets
    dump_pickle((X_train, y_train), os.path.join(dest_path, "train.pkl"))
    dump_pickle((X_test, y_test), os.path.join(dest_path, "test.pkl"))

if __name__ == '__main__':
    data_prep()