from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.coffe_keyboard import coffe_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list_coffe')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=coffe_keyboard,
        parse_mode="HTML"
    )