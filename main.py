import os
from dotenv import load_dotenv
from submit_task_service import send_answer
from transcriber import transcribe_files, prepare_prompt
from openai_service import OpenAiService

load_dotenv()
api_key = os.getenv("HEADQUARTERS_API_KEY")
open_ai_key = os.getenv("OPENAI_API_KEY")

transcriptions = transcribe_files(r"C:\Users\gajda\Downloads\przesluchania", open_ai_key)
print(transcriptions)
prompt = prepare_prompt(transcriptions)

openai_service = OpenAiService(open_ai_key)
print(openai_service.get_answer(prompt))




