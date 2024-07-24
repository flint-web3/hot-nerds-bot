from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import web_app_url


start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Our Public Channel", url="https://t.me/hot_nerds")],
        [InlineKeyboardButton(text="Open Web App", web_app={"url": web_app_url})],
    ]
)
