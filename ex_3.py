import os
from idlelib.iomenu import encoding
from io import text_encoding
from services import openai_service
import requests
from dotenv import load_dotenv
import json


def get_input_data(url: str):
    file_name = 'data.json'
    response = requests.get(url)
    response.raise_for_status()

    with open(file_name, 'w') as f:
        json.dump(response.json(), f)

    return file_name


def validate_and_correct_data(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    test_data = data.get("test-data", [])
    for item in test_data:
        question_text = item.get("question")

        answer = item.get("answer")
        test = item.get("test")
        correct_answer = evaluate_question(question_text)

        if test:
            print(f'Test question found: {test.get("q")}')
            test["a"] = openai_service.get_answer(test.get("q"))

        if answer != correct_answer:
            print(f"Incorrect answer found: {question_text}, {answer}")
            item['answer'] = correct_answer

    return data


def evaluate_question(question_text: str):
    return eval(question_text)


def send_answer(api_url, api_key, answer_data):
    answer_data["apikey"] = api_key
    data = {
        "task": "JSON",
        "apikey": api_key,
        "answer": answer_data
    }
    print(data)  # Możesz usunąć to w produkcji
    try:
        response = requests.post(api_url, json=data)  # Korzystamy z `json=data` do automatycznego kodowania na JSON
        response.raise_for_status()

        print("API answer: ", response.json())
    except requests.exceptions.RequestException as e:
        print("Error ---", e)
