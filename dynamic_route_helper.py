from flask import Flask, request, jsonify

from openai_service import OpenAiService
from dotenv import load_dotenv
import os
app = Flask(__name__)

load_dotenv()

def get_gtp_tip(openai_service: OpenAiService, description):
    context = f"""
        "context": "You are navigating a grid-based map with 12 squares organized in 4 rows and 3 columns. Each square has a distinct feature described below. Your starting position is row 1 column 1:",
        "map":
            "row_1":
                "square_1": "A location marker icon, representing a starting point or a significant location.",
                "square_2": "A grassy area with a single tree standing tall in the center.",
                "square_3": "A small house with a chimney, surrounded by grass."
            "row_2":
                "square_4": "A grassy area with no additional features.",
                "square_5": "A windmill with blades, surrounded by grass.",
                "square_6": "Another grassy area, empty of any structures."
            "row_3":
                "square_7": "A grassy field with no notable features.",
                "square_8": "A pile of rocks in the center, set in a grassy area.",
                "square_9": "Two trees standing close together, surrounded by grass."
            "row_4":
                "square_10": "A mountain range with multiple peaks.",
                "square_11": "A continuation of the mountain range, with sharp peaks and rugged terrain.",
                "square_12": "A car tilted at an angle near the entrance of a cave, with grass around."
        "instructions": "Answer in one word where the drone is located after the route description. Don't use coordinates just say what's on the location. Answer in polish."
    """

    return openai_service.get_answer(description, context)

@app.route('/my_api', methods=['POST'])
def my_api():
    data = request.get_json()
    instruction = data.get('instruction', '')
    print(instruction)

    openai_service = OpenAiService(os.getenv('OPENAI_API_KEY'))
    answer = get_gtp_tip(openai_service, instruction)
    print(answer)

    return jsonify({"description": answer})


if __name__ == '__main__':
    app.run(port=5000, debug=True)