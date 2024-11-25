import os
from ex_1 import get_question, submit_from
from ex_2 import start_verification
from ex_3 import validate_and_correct_data, get_input_data, send_answer
from services import openai_service
from dotenv import load_dotenv

load_dotenv()

def run_ex_1():
    question = get_question()
    submit_from(openai_service.get_answer(question))

def run_ex_2():
    start_verification()

def run_ex_3(url, api_key):
    data = get_input_data(url)
    json = validate_and_correct_data(data)

    send_answer(api_url, api_key, json)


load_dotenv()
api_url = 'https://centrala.ag3nts.org/report'
api_key = os.getenv("HEADQUARTERS_API_KEY")
url = f"https://centrala.ag3nts.org/data/{api_key}/json.txt"

