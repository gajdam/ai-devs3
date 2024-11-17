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
driver.get(url)

element = driver.find_element(By.XPATH, '//*[@id="human-question"]')
text_value = element.text
print(text_value)

response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-4"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Return only number" + text_value}
    ],
    temperature=0.7  # Adjusts randomness; 0.7 is moderate
)

answer = response['choices'][0]['message']['content'].strip()
print(answer)



driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[1]').send_keys(login)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[2]').send_keys(password)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/input[3]').send_keys(answer)

driver.find_element(By.XPATH, '//*[@id="submit"]').click()