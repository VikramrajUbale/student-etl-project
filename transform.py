from datetime import datetime

def transform_data(df):
    df = df[["id", "name"]]

    df["marks"] = df["id"].apply(
        lambda x: 90 if x > 5 else 70
    )
    df["grade"]= df["marks"].apply(lambda X:'A' if X >= 80 else 'B')
    df["INSERTED_DTTS"] = datetime.now()

    return df