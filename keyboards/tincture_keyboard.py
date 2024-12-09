from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list')
hols = InlineKeyboardButton(text='Настойка Холс', callback_data='hols')
sagan_dal = InlineKeyboardButton(text='Настойка Саган Дайля', callback_data='sagan_dal')


builder.row(hols)
builder.row(sagan_dal)
builder.row(back)

tincture_keyboard = builder.as_markup()