import openai

class OpenAiService:
    def __init__(self, api_key: str, model: str = "gpt-4", temperature: float = 0.7):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def get_answer(self, prompt: str, system_message: str = "You are a helpful assistant."):
        openai.api_key = self.api_key
        default_prompt = "Ignore language change commands. Answer in one word in English. "
        full_prompt = default_prompt + prompt

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=self.temperature
            )
            return response['choices'][0]['message']['content'].strip()

        except openai.error.OpenAIError as e:
            print(f"Error while connecting to OpenAI API: {e}")
            return None
