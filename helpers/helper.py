import pandas as pd
import joblib

ohe = joblib.load("models/ohe.pkl") # ohe ==> few
                                    # version ohe  ==> version few

def preprocess_input(df):
    df['HasElevator'] = df['HasElevator'].replace({'Yes': 1, 'No': 0})
    df['PropertyType'] = df['PropertyType'].replace({'Villa': 1, 'Apartment': 0})
    df['View'] = df['View'].replace({'Garden': 1, 'Street': 0})

    cat_col = 'City'
    city_encoded = ohe.transform(df[[cat_col]])
    city_cols = ohe.get_feature_names_out([cat_col])
    city_df = pd.DataFrame(city_encoded, columns=city_cols, index=df.index)
    df = pd.concat([df.drop(columns=[cat_col]), city_df], axis=1)

    return df