import json
from openai import OpenAI

from main import api_key

with open(r"./incorrect.txt", "r") as file:
    lines = file.readlines()

messages = []

for line in lines:
    line = line.strip()
    if line:
        message = {
            "messages": [
                {"role": "system", "content": "validate numbers"},
                {"role": "user", "content": line},
                {"role": "assistant", "content": "0"}
            ]
        }

        messages.append(message)

with open("output2.jsonl", "w") as json_file:
    for message in messages:
        json.dump(message, json_file)
        json_file.write("\n")


