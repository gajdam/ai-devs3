from ex_1 import get_question, submit_from
from ex_2 import start_verification
from services import openai_service


def run_ex_1():
    question = get_question()
    submit_from(openai_service.get_answer(question))

def run_ex_2():
    start_verification()

run_ex_2()