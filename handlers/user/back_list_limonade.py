from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.limonade_keyboard import limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list_limonade')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=limonade_keyboard,
        parse_mode="HTML"
    )