from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list')

latte = InlineKeyboardButton(text='🧊Айс латте', callback_data='latte')
tonik = InlineKeyboardButton(text='☕️Эспрессо тоник', callback_data='tonik')
shmel = InlineKeyboardButton(text='🐝Шмель', callback_data='shmel')
cherry_gad = InlineKeyboardButton(text='🍒Вишневый сад', callback_data='cherry_gad')


builder.row(latte)
builder.row(tonik)
builder.row(shmel)
builder.row(cherry_gad)

builder.row(back)

coffe_keyboard = builder.as_markup()
