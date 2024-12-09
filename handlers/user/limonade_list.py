from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.limonade_keyboard import limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'limonade')
async def manual_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери Приготовление',
        reply_markup=limonade_keyboard,
        parse_mode='HTML'
    )