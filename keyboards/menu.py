from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖼 Логотип"), KeyboardButton(text="✍️ Текст")],
        [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="📸 Обработать")]
    ],
    resize_keyboard=True
)
