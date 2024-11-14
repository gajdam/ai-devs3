import openai

from os import getenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
openai.api_key = getenv('OPENAI_API_KEY')
login = getenv('LOGIN')
password = getenv('PASSWORD')
url = 'https://xyz.ag3nts.org/'

def init_web():
    driver = webdriver.Edge()
    driver.get(url)

    return driver

def handle_login(driver):
    question_text = driver.find_element(By.XPATH, '//*[@id="human-question"]').text
    print(question_text)

    answer = get_gpt_answer(question_text)

    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[1]').send_keys(login)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[2]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[3]').send_keys(answer)

    driver.find_element(By.XPATH, '//*[@id="submit"]').click()

def get_gpt_answer(prompt_question):
    prompt = "Return number only " + prompt_question
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages= [
            { "role": "system", "content": "You are a helpful assistant." },
            { "role": "user", "content": prompt }
        ],
        temperature = 0.7 # Adjusts randomness; 07 is moderate
    )

    answer = response['choices'][0]['message']['content'].strip()
    print(answer)

    return answer
