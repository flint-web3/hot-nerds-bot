from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import web_app_url


start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🫂 Join the community", url="https://t.me/hot_nerds")],
        [InlineKeyboardButton(text="🤓 Open HOT Nerds!", web_app={"url": web_app_url})],
    ]
)
