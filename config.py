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
    token=os.getenv("BOT_KEY")
)

config = Config(llm=llm,
                bot=bot)