import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class LLMConfig:
    model: str
    api_key: str
    api_base_url: str

@dataclass
class BotConfig:
    token: str
    admin_ids: list[int]
    webhook_url: str
    webhook_path: str
    log_level: str

@dataclass
class Config:
    llm: LLMConfig
    bot: BotConfig

llm = LLMConfig(
    model=os.getenv("MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base_url=os.getenv("OPENROUTER_URL"),
)

bot = BotConfig(
    token="1234567890",
    admin_ids=[1234567890],
    webhook_url="https://your-domain.com",
    webhook_path="/webhook",
    log_level="INFO",
)

config = Config(llm=llm,
                bot=bot)