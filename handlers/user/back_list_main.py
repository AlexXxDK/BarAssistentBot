from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.coctails_keyboard import coctails_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list_main')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=coctails_keyboard,
        parse_mode="HTML"
    )