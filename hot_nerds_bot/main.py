import asyncio
from aiogram.filters import Command
from aiogram.types import Message

from settings import router, dp, bot
from keyboards import start_keyboard


@router.message(Command("start"))
async def start(message: Message):

    await message.answer(
        text="The bot is under development. Wait for the news.",
        reply_markup=start_keyboard,
    )


@router.message()
async def new_mes(message: Message):
    await start(message)


async def main():
    bot_info = await bot.get_me()
    print(bot_info)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
