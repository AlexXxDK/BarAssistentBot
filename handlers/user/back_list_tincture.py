from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.tincture_keyboard import tincture_keyboard


@dp.callback_query(lambda callback: callback.data == 'back_list_tincture')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись',
        reply_markup=tincture_keyboard,
        parse_mode="HTML"
    )