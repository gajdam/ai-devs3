from markitdown import MarkItDown
from openai_service import OpenAiService
from dotenv import load_dotenv
import os


# TODO make this program full "agent" it has more quality and efficient when user ask questions while running
md = MarkItDown()
result = md.convert(r"./notatnik-rafala.pdf")
print(result.text_content)

with open("notatnik-rafala.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)

load_dotenv()

openai_service = OpenAiService(os.getenv("OPENAI_API_KEY"))
file = r"./notatnik-rafala.md"
context = result.text_content

prompt = f"""
    "instruction": Based on the context, answer the following questions. Take into account all the facts given in the text, in particular, references to events. The dates required for the answer are not given verbatim in the text. They are only referred to relatively)
    "01": "Do którego roku przeniósł się Rafał",
    "02": "Kto wpadł na pomysł, aby Rafał przeniósł się w czasie?",
    "03": "Gdzie znalazł schronienie Rafał? Nazwij krótko to miejsce",
    "04": "Którego dnia Rafał ma spotkanie z Andrzejem? (format: YYYY-MM-DD)",
    "05": "Gdzie się chce dostać Rafał po spotkaniu z Andrzejem?"
        """

answer = openai_service.get_answer(prompt, context)
print(answer)