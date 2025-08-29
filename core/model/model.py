from openai import OpenAI
from dotenv import load_dotenv

import config

load_dotenv()


class LLM:
    def __init__(self):
        self._client = OpenAI(
            api_key=config.llm.api_key,
            base_url=config.llm.api_base_url
        )

    def get_llm_response(self, content: str):
        resp = self._client.chat.completions.create(
            model=config.llm.model,
            messages=[{"role": "user",
                       "content": content}],
            stream=False,
        )

        return resp.choices[0].message.content

llm = LLM()
