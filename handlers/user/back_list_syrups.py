from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.syrups_keyboard import syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list_syrups')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=syrups_keyboard,
        parse_mode="HTML"
    )