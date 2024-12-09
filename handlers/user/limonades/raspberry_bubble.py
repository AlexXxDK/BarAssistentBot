from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_limonade_keyboard import back_list_limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'raspberry_bubble')
async def bubble_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Лимонад Малина-Бабблгам')}</u>
        Сироп малина - 50мл
        Сироп Бабл гам - 20мл
        Сок лимона - 20мл
        Вод сл.газ до конца\n

        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_limonade_keyboard,
        parse_mode='HTML'
    )