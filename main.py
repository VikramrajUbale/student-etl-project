from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Extract started")
    df = extract_data()

    print("Transform started")
    transformed_df = transform_data(df)

    print("Load started")
    load_data(transformed_df)

    print("Pipeline completed")
    print("All Done")
    

run_pipeline()