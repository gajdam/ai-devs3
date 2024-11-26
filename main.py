import os
from ex_1 import get_question, submit_from
from ex_2 import start_verification
from ex_3 import validate_and_correct_data, get_input_data
from ex_5 import get_input_data, send_answer
from services import openai_service
from dotenv import load_dotenv

def run_ex_1():
    question = get_question()
    submit_from(openai_service.get_answer(question))

def run_ex_2():
    start_verification()

def run_ex_3(url, api_key):
    data = get_input_data(url)
    json = validate_and_correct_data(data)

    send_answer(api_url, api_key, json)

def run_ex_5(url: str):
    tmp = get_input_data(url)
    tmp = 'censor user data. Enter the word CENZURA in place of name, city and street and age. Return it as string without " characters' + tmp
    answer = openai_service.get_answer(tmp)
    send_answer(api_url, api_key, answer)

load_dotenv()
api_url = 'https://centrala.ag3nts.org/report'
api_key = os.getenv("HEADQUARTERS_API_KEY")
url = f"https://centrala.ag3nts.org/data/{api_key}/json.txt"
url2 = f"https://centrala.ag3nts.org/data/{api_key}/cenzura.txt"

run_ex_5(url2)