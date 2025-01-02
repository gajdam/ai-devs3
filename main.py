import os

from dotenv import load_dotenv

from keywords_process import process_reports
from submit_task_service import send_answer

load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")
directory_path = r"C:\Users\gajda\Downloads\pliki_z_fabryki"

process_reports(directory_path, openai_key)

