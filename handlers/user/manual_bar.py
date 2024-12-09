from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.manual_bar_keyboard import manual_bar_keyboard


@dp.callback_query(lambda callback: callback.data == 'manual_bar')
async def manual_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери Приготовление',
        reply_markup=manual_bar_keyboard,
        parse_mode='HTML'
    )