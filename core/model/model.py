from openai import OpenAI, APIError, APIConnectionError, Timeout
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential


import config

load_dotenv()


class LLM:
    def __init__(self):
        self._client = OpenAI(
            api_key=config.llm.api_key,
            base_url=config.llm.api_base_url
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def get_llm_response(self, content: str):
        try:
            resp = self._client.chat.completions.create(
                model=config.llm.model,
                messages=[{"role": "user", "content": content}],
                stream=False,
                timeout=30
            )
        except (APIError, APIConnectionError, Timeout) as e:
            raise RuntimeError(f"LLM API error: {e}")

        return resp.choices[0].message.content

llm = LLM()
