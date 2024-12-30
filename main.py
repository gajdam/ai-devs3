import os
from dotenv import load_dotenv
from numba.scripts.generate_lower_listing import description

from submit_task_service import send_answer
from transcriber import transcribe_files, prepare_prompt
from openai_service import OpenAiService
import requests


load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")
open_ai_key = os.getenv("OPENAI_API_KEY")

robot_description_url = f"https://centrala.ag3nts.org/data/{api_key}/robotid.json"


#
# transcriptions = transcribe_files(r"C:\Users\gajda\Downloads\przesluchania", open_ai_key)
# print(transcriptions)
# prompt = prepare_prompt(transcriptions)
#

def get_robot_description():
    response = requests.get(robot_description_url)
    if response.status_code == 200:
        return response.json().get("description")
    else:
        raise Exception(f"Failed to get robot description: {response.status_code}")


openai_service = OpenAiService(open_ai_key, "dall-e-3")
description = get_robot_description()
image_url = openai_service.generate_image(description)

print(image_url)
# print(openai_service.get_answer(prompt))




