from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list_limonade')

builder.row(back)

back_list_limonade_keyboard = builder.as_markup()
