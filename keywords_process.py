from openai_service import OpenAiService
import os
import json


def generate_keywords(file_path: str, openai_service: OpenAiService) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_name = os.path.basename(file_path)

    prompt = f"""
    File name: {file_name}, File content: {content}

    Generate keywords in the denominator form that best describe the person or any animals mentioned in this file. 
    The keywords should be separated by commas and be useful for searching in document retrieval systems.
    """

    keywords = openai_service.get_answer(prompt)
    return keywords


def save_data_to_file(data):
    output_file = fr"./data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def process_reports(directory_path: str, openai_key: str):
    data = {}

    openai_service = OpenAiService(openai_key)

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            print(f"processing file: {file_name}")
            data[file_name] = generate_keywords(file_path, openai_service)

    save_data_to_file(data)
    return data