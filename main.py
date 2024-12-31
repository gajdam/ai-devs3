import base64
import os
from dotenv import load_dotenv
from submit_task_service import send_answer
from openai_service import OpenAiService
import requests

load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")
open_ai_key = os.getenv("OPENAI_API_KEY")

robot_description_url = f"https://centrala.ag3nts.org/data/{api_key}/robotid.json"
# TODO refactor s2d4
# TODO fix analyzing images - sometimes works

# s2e1
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


### s2e3
# openai_service = OpenAiService(open_ai_key, "dall-e-3")
# description = get_robot_description()
# image_url = openai_service.generate_image(description)
# print(image_url)

folder_path = r"C:\Users\gajda\Downloads\pliki_z_fabryki"
classified_files = {"people": [], "hardware": []}
openai_service = OpenAiService(open_ai_key)


def encode_image(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None


def get_files(folder_path: str) -> list:
    files_to_process = []
    for root, dirs, files in os.walk(folder_path):
        if "facts" in root:
            continue
        for file in files:
            files_to_process.append(os.path.join(root, file))
    return files_to_process


def analyze_file(file: str, openai_service: OpenAiService) -> str:
    ext = os.path.splitext(file)[1]
    try:
        if ext == ".mp3":
            content = openai_service.transcribe_audio(file)
        elif ext == ".txt":
            with open(file, "r") as f:
                content = f.read()
        elif ext == ".png":
            image_base64 = encode_image(file)
            content = openai_service.analyze_image(image_base64, "Describe the image content.")
        else:
            return "none"

        # Use unified prompt for categorization
        prompt = f"""
            Analyze the following content from file '{file}' and determine if it mentions any of the following:
            1. Captured people, traces of their presence, or descriptions of their hostile activity.
            2. Fixed hardware malfunctions (ignore software issues).
            Respond with one word only: "people" if it mentions captured people, traces of their presence, or descriptions of their hostile activity; "hardware" if it mentions fixed hardware malfunctions; or "none" if neither is mentioned.

            Please extract for us only notes containing information about captured people, traces of their presence, or descriptions of their hostile activity.

            Content: {content}
            """

        return openai_service.get_answer(prompt)
    except Exception as e:
        print(f"Error analyzing file {file}: {e}")
        return "none"


# Main Execution
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai_service = OpenAiService(api_key)
folder_path = r"C:\Users\gajda\Downloads\pliki_z_fabryki"

files = get_files(folder_path)
classified_files = {"people": [], "hardware": []}

for file in files:
    category = analyze_file(file, openai_service)
    if category in classified_files:
        file_name = os.path.basename(file)
        classified_files[category].append(file_name)
        print(f"Added {file_name} to category {category}.")
    else:
        print(f"Category '{category}' does not exist.")

print("Final Classified Files:", classified_files)
