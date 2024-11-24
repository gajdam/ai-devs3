import os
from dotenv import load_dotenv
from openai_service import OpenAiService

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai_service = OpenAiService(api_key)
