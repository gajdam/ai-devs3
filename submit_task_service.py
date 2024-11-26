import requests

def send_answer(task_name: str, api_key: str, answer):
    data = {
        "task": task_name,
        "apikey": api_key,
        "answer": answer
    }

    try:
        response = requests.post('https://centrala.ag3nts.org/report', json=data)
        response.raise_for_status()

        print("API answer: ", response.json())
    except requests.exceptions.RequestException as e:
        print("Error ---", e)