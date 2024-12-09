from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.coffe_keyboard import coffe_keyboard


@dp.callback_query(lambda callback: callback.data == 'coffe')
async def manual_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери Приготовление',
        reply_markup=coffe_keyboard,
        parse_mode='HTML'
    )