import os
import openai
import requests
from dotenv import load_dotenv
import json


def get_input_data(url: str) -> list:
    response = requests.get(url)
    response.raise_for_status()
    test_data = response.json().get('test-data', [])

    return test_data


def analyze_questions(questions_list: list) -> list:
    corrected_questions = []

    for question in questions_list:
        question_text = question.get('question')

        answer = question.get('answer')
        test = question.get('test')

        if test:
            print(f'Test question found: {test.get('q')}')
            # test.get['a'] = get_gpt_answer(test.get('q'))

        if answer != eval(question_text):
            print(f"Incorrect answer found: {question_text}, {answer}")
            question['answer'] = eval(question_text)

        print(question)


load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")
url = f"https://centrala.ag3nts.org/data/{api_key}/json.txt"

questions = get_input_data(url)
analyze_questions(questions)
