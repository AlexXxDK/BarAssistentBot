from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list')

sea_buckthorn = InlineKeyboardButton(text='Облепиха', callback_data='sea_buckthorn')
currant = InlineKeyboardButton(text='Смородина', callback_data='сurrant')
mandarin = InlineKeyboardButton(text='🍊Мандарин', callback_data='mandarin')
sugar = InlineKeyboardButton(text='Сахарный', callback_data='sugar')
apple = InlineKeyboardButton(text='🍎Пряное Яблоко', callback_data='apple')
raspberries = InlineKeyboardButton(text='Малина', callback_data='raspberries')

builder.row(sea_buckthorn, currant)
builder.row(mandarin, sugar)
builder.row(apple, raspberries)
builder.row(back)

syrups_keyboard = builder.as_markup()