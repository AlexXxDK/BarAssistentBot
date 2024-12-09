from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.manual_bar_keyboard import manual_bar_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=manual_bar_keyboard,
        parse_mode="HTML"
    )