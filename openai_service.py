from openai import OpenAI

class OpenAiService:
    def __init__(self, api_key: str, model: str = "gpt-4", temperature: float = 0.7):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature

    def get_answer(self, prompt: str, system_message: str = "You are a helpful assistant.") -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error while connecting to OpenAI API: {e}")
            return None

    def analyze_image(self, image_base64: str, prompt: str):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                }
                            },
                        ],
                    }
                ],
            )
            return completion.choices[0].message
        except Exception as e:
            print(f"Error while analyzing image: {e}")
            return None

    def transcribe_audio(self, file_path: str) -> str:
        try:
            with open(file_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            return transcription.text
        except Exception as e:
            print(f"Error while transcribing audio: {e}")
            return None

    def generate_image(self, prompt: str) -> str:
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024", # change to parameter
                quality="standard",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error while generating image: {e}")
            return None

    def generate_embedding(self, input: str):
        completion = self.client.embeddings.create(
            model="text-embedding-ada-002",
            input=input
        )
        return completion.data[0].embedding