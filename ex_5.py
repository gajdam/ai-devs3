import requests

def get_input_data(url: str):
    response = requests.get(url)
    response.raise_for_status()

    print(response.text)
    return response.text


def send_answer(api_url, api_key, answer_data):
    data = {
        "task": "CENZURA",
        "apikey": api_key,
        "answer": answer_data
    }
    print(data)
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()
        print(response.headers)
        print("API answer: ", response.json())
    except requests.exceptions.RequestException as e:
        print("Error ---", e)