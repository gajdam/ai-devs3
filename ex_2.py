import requests
from services import openai_service

def start_verification():
    # Start communication with the robot by sending the "READY" command
    url = "https://xyz.ag3nts.org/verify"
    data = {
        "text": "READY",
        "msgID": "0",
    }

    response = requests.post(url, json=data)
    print(response)
    print(response.text)

    robot_response = response.json()

    print(robot_response["text"])
    print(robot_response["msgID"])

    answer = get_response(robot_response["text"])

    data = {"text": answer,
            "msgID": robot_response["msgID"]}
    response = requests.post(url, json=data)
    print(response.text)


def get_response(response):
    if "capital of poland?" in response.lower():
        answer = "Kraków"
    elif "what year is it" in response.lower():
        answer = "1999"
    elif "the hitchhiker's" in response.lower():
        answer = "69"
    else:
        answer = openai_service.get_answer(response)
    print(answer)
    return answer


