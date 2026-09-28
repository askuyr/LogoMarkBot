from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda m: m.text == "🖼 Логотип")
async def logo(message: Message):
    await message.answer("Отправьте PNG или JPG логотип.")
