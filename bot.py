import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from handlers.logo import router as logo_router
from handlers.photo import router as photo_router
from handlers.settings import router as settings_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing in .env")

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(logo_router)
    dp.include_router(photo_router)
    dp.include_router(settings_router)

    print("LogoMarkBot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
