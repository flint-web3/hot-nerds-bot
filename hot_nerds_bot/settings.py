import logging
from pydantic_settings import BaseSettings
from typing import Optional
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    tg_token: str
    web_app_url: str

    bot: Optional[Bot] = None
    dp: Optional[Dispatcher] = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = Bot(token=self.tg_token)
        self.dp = Dispatcher(storage=MemoryStorage())

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
bot = settings.bot
dp = settings.dp
router = Router()
web_app_url = settings.web_app_url
