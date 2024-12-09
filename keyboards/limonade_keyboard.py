from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list')
cherry_elder = InlineKeyboardButton(text='🍒Вишня-Бузина', callback_data='cherry_elder')
raspberry_bubble = InlineKeyboardButton(text='Малина-Бабблгам', callback_data='raspberry_bubble')
passion_fruit_jasmine = InlineKeyboardButton(text='Маракуйя-Жасмин', callback_data='passion_fruit_jasmine')
sea_buckthorn_mint = InlineKeyboardButton(text='Облепиха-Мята', callback_data='sea_buckthorn_mint')

builder.row(cherry_elder, raspberry_bubble)
builder.row(passion_fruit_jasmine, sea_buckthorn_mint)


builder.row(back)

limonade_keyboard = builder.as_markup()