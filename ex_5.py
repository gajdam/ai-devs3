import requests

def get_input_data(url: str):
    response = requests.get(url)
    response.raise_for_status()

    print(response.text)
    return response.text