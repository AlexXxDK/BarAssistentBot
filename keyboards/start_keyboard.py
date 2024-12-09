from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

manual_bar = InlineKeyboardButton(text='🍸Найти Рецепт', callback_data='manual_bar')
bar_menu = InlineKeyboardButton(text='🔍Посмотреть меню бара', callback_data='bar_menu')

builder.row(manual_bar)
builder.row(bar_menu)

start_keyboard = builder.as_markup()




