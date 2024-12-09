from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.start_keyboard import start_keyboard


@dp.callback_query(lambda callback: callback.data == 'back')
async def back_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Вы вернулись в главное меню',
        reply_markup=start_keyboard,
        parse_mode="HTML"
    )