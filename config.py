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
class DatabaseConfig:
    user: str
    password: str
    host: str
    port: str
    db_name: str
    
    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

@dataclass
class JWTConfig:
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

@dataclass
class Config:
    llm: LLMConfig
    bot: BotConfig
    database: DatabaseConfig
    jwt: JWTConfig

llm = LLMConfig(
    model=os.getenv("MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base_url=os.getenv("OPENROUTER_URL"),
)

bot = BotConfig(
    token=os.getenv("BOT_KEY")
)

database = DatabaseConfig(
    user=os.getenv("DB_USER", ""),
    password=os.getenv("DB_PASSWORD", ""),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432"),
    db_name=os.getenv("DB_NAME", "app")
)

jwt = JWTConfig(
    secret_key=os.getenv("JWT_SECRET_KEY", "your-secret-key"),
    algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
    access_token_expire_minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
)

config = Config(llm=llm,
                bot=bot,
                database=database,
                jwt=jwt)