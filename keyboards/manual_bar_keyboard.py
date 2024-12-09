from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back')

coctails = InlineKeyboardButton(text='🍸Коктейли', callback_data='coctails')
tincture = InlineKeyboardButton(text='🥃Настойки', callback_data='tincture')
syrups = InlineKeyboardButton(text='🍓Заготовки', callback_data='syrups')
limonade = InlineKeyboardButton(text='🍹Лимонады', callback_data='limonade')
coffe = InlineKeyboardButton(text='☕️Кофе', callback_data='coffe')


builder.row(coctails)
builder.row(tincture)
builder.row(syrups)
builder.row(limonade)
builder.row(coffe)

builder.row(back)

manual_bar_keyboard = builder.as_markup()
