from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.coctails_keyboard import coctails_keyboard


@dp.callback_query(lambda callback: callback.data == 'coctails')
async def manual_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери Приготовление',
        reply_markup=coctails_keyboard,
        parse_mode='HTML'
    )