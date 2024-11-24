import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
url = 'https://xyz.ag3nts.org/'
url2 = 'https://xyz.ag3nts.org/login'

driver = webdriver.Edge()

def get_question() -> str:
    driver.get(url)
    element = driver.find_element(By.XPATH, '//*[@id="human-question"]')
    text_value = element.text
    print(text_value)
    return text_value

def submit_from(answer: str):
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[1]').send_keys(login)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[2]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[3]').send_keys(answer)

    driver.find_element(By.XPATH, '//*[@id="submit"]').click()