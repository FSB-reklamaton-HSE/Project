"""
Модуль для работы с клавиатурами в aiogram.

Содержит функции для создания:
- Inline-клавиатур с категориями
- Кнопки добавления карты
- Reply-клавиатуры для завершения ввода
"""

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
    
    
def ikb_start_desription() -> InlineKeyboardMarkup:
    """
    Создает inline-кнопку с кнопкой начала опроса.
    
    Returns:
        InlineKeyboardMarkup: Клавиатура с одной кнопкой
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Начать опрос", 
                callback_data="start_desription"
            )]
        ],
        resize_keyboard=True,
        row_width=1
    )


def rkb_back_question() -> ReplyKeyboardMarkup:
    """
    Создает reply-клавиатуру с кнопкой завершения ввода.
    
    Returns:
        ReplyKeyboardMarkup: Клавиатура с одной кнопкой
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True,
        row_width=1
    )

