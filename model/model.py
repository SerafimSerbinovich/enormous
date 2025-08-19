import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self):
        self._client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url=os.getenv("OPENROUTER_URL")
        )

    def get_llm_response(self, content: str):
        resp = self._client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[{"role": "user",
                       "content": content}],
            stream=False,
        )

        return resp.choices[0].message.content

llm = LLM()
