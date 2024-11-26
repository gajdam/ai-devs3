import os
from dotenv import load_dotenv
from submit_task_service import send_answer

load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")

