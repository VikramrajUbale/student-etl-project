import requests
import pandas as pd

def extract_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)

    return df