import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def get_Data(data_type):
    y_data = []
    if data_type == "train":
        train_data = pd.read_csv("data//rec.csv")
        for call_type in train_data['cmt']:
            y_data.append(1) if call_type == "type1" else y_data.append(0)
        x_data = train_data.drop('cmt', axis=1)
        column_names = x_data.columns
        for i in range(13):
            if i < 2:
                continue
            column_to_encode = column_names[i]
            label_encoder = LabelEncoder()
            x_data[column_to_encode] = label_encoder.fit_transform(x_data[column_to_encode])
            # One-hot encoding
            final_x = x_data.values
        return final_x, y_data
    else:
        test_data = pd.read_csv("data//test.csv")
        x_data = test_data
        column_names = x_data.columns
        for i in range(13):
            if i < 2:
                continue
            column_to_encode = column_names[i]
            label_encoder = LabelEncoder()
            x_data[column_to_encode] = label_encoder.fit_transform(x_data[column_to_encode])
            df_cleaned = x_data.dropna(axis=0)
        return df_cleaned, y_data
