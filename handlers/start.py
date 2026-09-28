from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.menu import menu

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в LogoMarkBot!\n\n"
        "Добавляйте логотип и текст на свои изображения.",
        reply_markup=menu
    )
